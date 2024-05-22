def display_todos(todos):
    """할 일 목록을 표시하는 함수"""
    if not todos:
        print("할 일이 없습니다!")
    else:
        print("\n할 일 목록:")
        for idx, todo in enumerate(todos, 1):
            print(f"{idx}. {todo}")
    print()

def add_todo():
    """할 일을 추가하는 함수"""
    new_todo = input("추가할 할 일을 입력하세요: ")
    todos.append(new_todo)
    print(f"'{new_todo}'가 추가되었습니다.\n")

def delete_todo():
    """할 일을 삭제하는 함수"""
    display_todos(todos)
    try:
        todo_number = int(input("삭제할 할 일 번호를 입력하세요: "))
        if 1 <= todo_number <= len(todos):
            removed_todo = todos.pop(todo_number - 1)
            print(f"'{removed_todo}'가 삭제되었습니다.\n")
        else:
            print("유효하지 않은 번호입니다.\n")
    except ValueError:
        print("숫자를 입력하세요.\n")

def main():
    """메인 함수"""
    while True:
        print("1. 할 일 추가")
        print("2. 할 일 삭제")
        print("3. 할 일 목록 보기")
        print("4. 종료")
        choice = input("원하는 작업을 선택하세요 (1/2/3/4): ")

        if choice == '1':
            add_todo()
        elif choice == '2':
            delete_todo()
        elif choice == '3':
            display_todos(todos)
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택하세요.\n")

# 프로그램 실행
if __name__ == "__main__":
    todos = []
    main()
