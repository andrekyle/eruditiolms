"""Extract Python code blocks from agent report files and write the data files."""
import re
import sys
from pathlib import Path

BASE = Path(r"c:\Users\hp\AppData\Roaming\Code\User\workspaceStorage\25f723a0a07d7e81c8ab2371048eef31\GitHub.copilot-chat\chat-session-resources\4bab04b0-1fcb-46c2-a2db-33b4ae5fb628")
OUT = Path(r"c:\Users\hp\Documents\lms - Amazing 19\_java_oca_authoring")

MAP = {
    'toolu_vrtx_018ZoeWZDwXj1Ux3tjYXXKBZ__vscode-1779290622492': 'l9_api_classes.py',
    'toolu_vrtx_01WcYQMViMDEwWeQqExhQutG__vscode-1779290622493': 'final_exam.py',
}

# Match the LARGEST ```python ...``` block in each report
BLOCK_RE = re.compile(r'```python\s*\n(.*?)\n```', re.DOTALL)

for folder, fname in MAP.items():
    src = BASE / folder / 'content.txt'
    if not src.exists():
        print(f'SKIP {fname}: source missing {src}')
        continue
    text = src.read_text(encoding='utf-8')
    blocks = BLOCK_RE.findall(text)
    if not blocks:
        print(f'FAIL {fname}: no python code block')
        continue
    # Take the largest block (it's the actual data)
    code = max(blocks, key=len)
    dst = OUT / fname
    dst.write_text(code, encoding='utf-8')
    # Validate by importing
    import importlib.util
    spec = importlib.util.spec_from_file_location(dst.stem, dst)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f'FAIL {fname}: import error: {e}')
        continue
    if fname == 'final_exam.py':
        qs = getattr(mod, 'QUESTIONS', None)
        ok = isinstance(qs, list) and len(qs) == 25
        print(f'{"OK " if ok else "FAIL"} {fname}: {len(dst.read_text(encoding="utf-8"))} bytes, QUESTIONS={len(qs) if isinstance(qs,list) else "??"}')
    else:
        html = getattr(mod, 'LESSON_HTML', None)
        qs = getattr(mod, 'QUESTIONS', None)
        ok = isinstance(html, str) and isinstance(qs, list) and len(qs) == 8
        print(f'{"OK " if ok else "FAIL"} {fname}: {len(dst.read_text(encoding="utf-8"))} bytes, LESSON_HTML={len(html) if isinstance(html,str) else "??"}, QUESTIONS={len(qs) if isinstance(qs,list) else "??"}')

sys.exit(0)
