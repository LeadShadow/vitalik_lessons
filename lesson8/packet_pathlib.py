from pathlib import Path

p = Path('C:/Users/pc/Desktop/заняття/vitalik_lessons/lesson8')
print(p)

print(p.parent)
print(p.name)
print(p.suffix)
print(p.exists())
print(p.is_dir())
print(p.is_file())

for i in p.iterdir():
    print(i)

