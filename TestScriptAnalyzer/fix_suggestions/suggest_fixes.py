import re, os, sys

def suggest_replace_sleep(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'time.sleep' in content:
        print(f"Suggested fix for {file_path}: replace hard waits with explicit locator waits. Example:")
        print("page.locator('selector').wait_for(state='visible', timeout=10000)  # then interact")
    else:
        print("No simple fixes detected.")

if __name__ == '__main__':
    for p in sys.argv[1:]:
        suggest_replace_sleep(p)
