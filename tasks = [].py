tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✔️ کار '{task}' اضافه شد.")

def show_tasks():
    if not tasks:
        print("📭 لیست کارها خالیه!")
    else:
        print("📋 لیست کارها:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n۱. اضافه کردن کار")
    print("۲. نمایش لیست کارها")
    print("۳. خروج")

    choice = input("انتخاب کن (1/2/3): ")

    if choice == '1':
        task = input("چی می‌خوای به لیست اضافه کنی؟ ")
        add_task(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        print("خروج از برنامه. خداحافظ! 👋")
        break
    else:
        print("❌ گزینه نامعتبره.")
