import streamlit as st

# 할 일 리스트를 저장할 빈 리스트 선언
if 'to_do_list' not in st.session_state:
    st.session_state['to_do_list'] = []

def add_task(task):
    if task:  # 입력된 할 일이 있을 경우에만 추가
        st.session_state['to_do_list'].append(task)
        st.success(f"'{task}' 할 일이 추가되었습니다.")
        # 할 일 추가 후 입력 필드 초기화
        st.session_state['add_task_input'] = ""

def delete_task(task_number):
    try:
        if task_number and 0 < task_number <= len(st.session_state['to_do_list']):
            removed_task = st.session_state['to_do_list'].pop(task_number - 1)
            st.success(f"'{removed_task}' 할 일이 삭제되었습니다.")
        else:
            st.error("유효하지 않은 번호입니다.")
    except ValueError:
        st.error("유효한 번호를 입력하세요.")

def view_tasks():
    if st.session_state['to_do_list']:
        for idx, task in enumerate(st.session_state['to_do_list'], start=1):
            st.write(f"{idx}. {task}")
    else:
        st.write("할 일이 없습니다.")

def main():
    st.title("To-Do List")

    with st.sidebar:
        st.header("메뉴")
        # 할 일 추가 입력 필드에 st.session_state 사용
        add_task_input = st.text_input("할 일 추가", key="add_task_input")
        if st.button("추가"):
            add_task(add_task_input)

        # 할 일 삭제 입력 필드의 max_value 수정
        if st.session_state['to_do_list']:
            delete_task_input = st.number_input("할 일 삭제 (번호 입력)", 
                                                min_value=1, 
                                                max_value=len(st.session_state['to_do_list']), 
                                                step=1, 
                                                key="delete_task_input")
            if st.button("삭제"):
                delete_task(int(delete_task_input))
        else:
            st.write("삭제할 할 일이 없습니다.")
    
    st.header("현재 할 일 목록")
    view_tasks()

if __name__ == "__main__":
    main()
