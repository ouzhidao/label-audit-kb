#!/usr/bin/env python3
"""
标签审核统计报表
用法: python 统计报表.py [--period 2026-05] [--factory DWT] [--client 瑞幸]
输出: 控制台 + _统计报告.md
"""
import json, os, sys, re
from collections import Counter, defaultdict
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
CHAINS = os.path.join(BASE, '版本链')
INDEX = os.path.join(CHAINS, '_版本索引.json')

def load_data():
    products = []
    with open(INDEX, 'r', encoding='utf-8') as f:
        idx = json.load(f)
    
    for p in idx.get('products', []):
        pid = p['product_id']
        chain_file = os.path.join(CHAINS, pid, 'version_chain.json')
        if not os.path.exists(chain_file):
            products.append(p)
            continue
        
        with open(chain_file, 'r', encoding='utf-8') as f:
            chain = json.load(f)
        
        for v in chain.get('versions', []):
            products.append({
                'product_id': pid,
                'name': p.get('name', '?'),
                'client': p.get('client', '?'),
                'spec': p.get('spec', '?'),
                'version': v.get('version', '?'),
                'date': v.get('date', '?'),
                'issues_found': v.get('issues_found', 0),
                'issues_detail': v.get('issues_detail', []),
            })
    return products

def stats_by_factory(products):
    factories = defaultdict(lambda: {'total': 0, 'with_issues': 0, 'issues': Counter()})
    for p in products:
        pid = p['product_id']
        if '_DWT_' in pid or 'DWT' in pid.upper(): f = 'DWT'
        elif '_LYG_' in pid or 'LYG' in pid.upper(): f = 'LYG'
        elif '_LKE_' in pid or 'LKE' in pid.upper(): f = 'LKE'
        elif '_HK_' in pid or 'LYGHB' in pid: f = 'LYGHB'
        else: f = '其他'
        
        fac = factories[f]
        fac['total'] += 1
        if p['issues_found'] > 0:
            fac['with_issues'] += 1
        for d in p.get('issues_detail', []):
            cat = d.split(':')[0] if ':' in d else d
            fac['issues'][cat] += 1
    return factories

def stats_by_period(products):
    months = defaultdict(lambda: {'total': 0, 'with_issues': 0})
    for p in products:
        if len(p['date']) >= 7:
            month = p['date'][:7]
            months[month]['total'] += 1
            if p['issues_found'] > 0:
                months[month]['with_issues'] += 1
    return dict(sorted(months.items()))

def top_issues(products):
    issues = Counter()
    for p in products:
        for d in p.get('issues_detail', []):
            issues[d] += 1
    return issues.most_common(10)

def generate_report(products):
    lines = []
    lines.append('# 标签审核统计报表')
    lines.append('')
    lines.append(f'> 生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}')
    lines.append(f'> 总审核数：{len(products)} 次')

    total_issues = sum(p['issues_found'] for p in products)
    lines.append(f'> 问题总数：{total_issues} 个')

    # By factory
    factories = stats_by_factory(products)
    lines.append('')
    lines.append('## 按工厂统计')
    lines.append('')
    lines.append('| 工厂 | 审核数 | 有问题 | 问题率 | 高频问题 |')
    lines.append('|------|:--:|:--:|:--:|------|')
    for f, d in sorted(factories.items()):
        rate = f"{d['with_issues']/d['total']*100:.0f}%" if d['total'] > 0 else '-'
        top = ', '.join([f"{k}({v})" for k, v in d['issues'].most_common(3)])
        lines.append(f"| {f} | {d['total']} | {d['with_issues']} | {rate} | {top or '-'} |")

    # By month
    months = stats_by_period(products)
    lines.append('')
    lines.append('## 按月份趋势')
    lines.append('')
    lines.append('| 月份 | 审核数 | 有问题 | 问题率 |')
    lines.append('|------|:--:|:--:|:--:|')
    for m, d in months.items():
        rate = f"{d['with_issues']/d['total']*100:.0f}%" if d['total'] > 0 else '-'
        lines.append(f"| {m} | {d['total']} | {d['with_issues']} | {rate} |")

    # Top issues
    top = top_issues(products)
    if top:
        lines.append('')
        lines.append('## 高频问题 TOP10')
        lines.append('')
        lines.append('| 问题 | 次数 |')
        lines.append('|------|:--:|')
        for issue, count in top:
            lines.append(f"| {issue} | {count} |")

    return '\n'.join(lines)

if __name__ == '__main__':
    products = load_data()
    if not products:
        print('无审计记录')
        sys.exit(0)
    
    report = generate_report(products)
    
    # Print to console
    print(report)
    
    # Save to file
    out = os.path.join(BASE, '_统计报告.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(report)
    print('')
    print(f'报表已保存: {out}')
