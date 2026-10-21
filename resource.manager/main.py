import json
FILE='resources.json'
def load_records():
    try:
        with open(FILE,'r',encoding='utf-8')as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_records(records):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def show_records(records):
    if not records:
        print("暂无资料")
        return
    for i, r in enumerate(records, 1):
        print(f"{i}. {r['title']}")
        print(f"   {r['url']}\n")

def main():
    records = load_records()          # 启动时只读一次
    while True:
        print("\n学习资料记录本")
        print(f"已加载 {len(records)} 条资料。")
        print("1. 查看所有资料\n2. 添加资料\n0. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            show_records(records)
        elif choice == "2":
            title = input("请输入资料名称：").strip()
            url = input("请输入资料链接：").strip()
            if not title or not url:
                print("名称和链接都不能为空")
                continue
            records.append({"title": title, "url": url})
            save_records(records)     # 保存的是完整列表
            print("添加成功，已保存。")
        elif choice == "0":
            break
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    main()

