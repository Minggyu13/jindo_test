# import streamlit as st

# st.text("hello world")


# to_do_list.py

# 할 일 리스트를 저장할 빈 리스트 선언
to_do_list = []

def show_menu():
    print("\nTo-Do List 메뉴:")
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 모든 할 일 보기")
    print("4. 종료")

def add_task():
    task = input("추가할 할 일을 입력하세요: ")
    to_do_list.append(task)
    print(f"'{task}' 할 일이 추가되었습니다.")

def delete_task():
    if not to_do_list:
        print("삭제할 할 일이 없습니다.")
        return

    show_tasks()
    try:
        task_number = int(input("삭제할 할 일 번호를 입력하세요: ")) - 1
        if 0 <= task_number < len(to_do_list):
            removed_task = to_do_list.pop(task_number)
            print(f"'{removed_task}' 할 일이 삭제되었습니다.")
        else:
            print("유효하지 않은 번호입니다.")
    except ValueError:
        print("유효한 번호를 입력하세요.")

def show_tasks():
    if not to_do_list:
        print("할 일이 없습니다.")
    else:
        print("\n현재 할 일 목록:")
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{idx}. {task}")

def main():
    while True:
        show_menu()
        choice = input("메뉴에서 선택하세요: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효하지 않은 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
