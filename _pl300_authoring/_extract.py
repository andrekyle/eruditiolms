"""Extract Python code blocks from PL-300 author agent reports and write the data files."""
import importlib.util
import re
import sys
from pathlib import Path

BASE = Path(r"c:\Users\hp\AppData\Roaming\Code\User\workspaceStorage\25f723a0a07d7e81c8ab2371048eef31\GitHub.copilot-chat\chat-session-resources\4bab04b0-1fcb-46c2-a2db-33b4ae5fb628")
OUT = Path(r"c:\Users\hp\Documents\lms - Amazing 19\_pl300_authoring")

MAP = {
    'toolu_vrtx_013FBDhizYfqUXy1joLzRm78__vscode-1779290622575': 'l1_get_data.py',
    'toolu_vrtx_017cz1PZzQm9bwskqNBfLcve__vscode-1779290622576': 'l2_transform.py',
    'toolu_vrtx_011dAX4KsxaqcX7iuBDXFbQ4__vscode-1779290622577': 'l3_design_model.py',
    'toolu_vrtx_01RgWHLaAixPCrwfvbVbu3Ze__vscode-1779290622578': 'l4_dax.py',
    'toolu_vrtx_01GCCmig76FHgfkNeaEJaPHd__vscode-1779290622579': 'l5_optimize.py',
    'toolu_vrtx_01VWcxLFNF3h7cmC2Xk9jRPt__vscode-1779290622580': 'l6_visualizations.py',
    'toolu_vrtx_018Pu5yboeGaWYP2X5f83kcH__vscode-1779290622581': 'l7_enhance.py',
    'toolu_vrtx_01JEBuzmm7HjxsWNRQe6CGLY__vscode-1779290622582': 'l8_analytics.py',
    'toolu_vrtx_01VY6dUfXXdH2SSQrMyvbFbE__vscode-1779290622583': 'l9_deploy.py',
    'toolu_vrtx_01XXtDwSAuXLcvEdeo1CJjRc__vscode-1779290622584': 'final_exam.py',
}

BLOCK_RE = re.compile(r'```python\s*\n(.*?)\n```', re.DOTALL)

for folder, fname in MAP.items():
    src = BASE / folder / 'content.txt'
    if not src.exists():
        print(f'SKIP {fname}: source missing')
        continue
    text = src.read_text(encoding='utf-8')
    blocks = BLOCK_RE.findall(text)
    if not blocks:
        print(f'FAIL {fname}: no python block')
        continue
    code = max(blocks, key=len)
    # Strip NUL bytes
    if '\x00' in code:
        nul_count = code.count('\x00')
        code = code.replace('\x00', '\\u0000')
        print(f'  ! stripped {nul_count} NULs from {fname}')
    dst = OUT / fname
    dst.write_text(code, encoding='utf-8')
    # Try import
    spec = importlib.util.spec_from_file_location(dst.stem, dst)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f'FAIL {fname}: import error: {type(e).__name__}: {e}')
        continue
    if fname == 'final_exam.py':
        qs = getattr(mod, 'QUESTIONS', None)
        n = len(qs) if isinstance(qs, list) else -1
        print(f'{"OK " if n == 25 else "??"} {fname}: bytes={dst.stat().st_size} QUESTIONS={n}')
    else:
        html = getattr(mod, 'LESSON_HTML', None)
        qs = getattr(mod, 'QUESTIONS', None)
        nq = len(qs) if isinstance(qs, list) else -1
        nh = len(html) if isinstance(html, str) else -1
        ok = nq == 8 and nh > 500
        print(f'{"OK " if ok else "??"} {fname}: bytes={dst.stat().st_size} LESSON_HTML={nh} QUESTIONS={nq}')

sys.exit(0)
