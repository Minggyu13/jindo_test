import streamlit as st

# 할 일 목록을 저장할 세션 상태 초기화
if 'to_do_list' not in st.session_state:
    st.session_state['to_do_list'] = []

# 할 일 추가 함수
def add_task():
    task = st.session_state.add_task_input  # 입력 필드의 값을 가져옴
    if task:  # 입력이 있는 경우에만 추가
        st.session_state['to_do_list'].append(task)
        st.success(f"'{task}' 할 일이 추가되었습니다.")
        st.session_state.add_task_input = ""  # 입력 필드를 초기화

# 할 일 삭제 함수
def delete_task(task_number):
    try:
        if task_number and 0 < task_number <= len(st.session_state['to_do_list']):
            removed_task = st.session_state['to_do_list'].pop(task_number - 1)
            st.success(f"'{removed_task}' 할 일이 삭제되었습니다.")
        else:
            st.error("잘못된 번호입니다.")
    except ValueError:
        st.error("유효한 번호를 입력하세요.")

# 할 일 목록 보기 함수
def view_tasks():
    if st.session_state['to_do_list']:
        for idx, task in enumerate(st.session_state['to_do_list'], start=1):
            st.write(f"{idx}. {task}")
    else:
        st.write("할 일이 없습니다.")

# 메인 함수
def main():
    st.title("할 일 목록")

    with st.sidebar:
        st.header("메뉴")
        # 할 일 추가 입력 필드
        st.text_input("할 일 추가", key="add_task_input")
        if st.button("추가"):
            add_task()

        # 할 일 삭제 입력 필드
        task_count = len(st.session_state['to_do_list'])
        delete_task_input = st.number_input("할 일 삭제 (번호 입력)", 
                                            min_value=1, 
                                            max_value=task_count, 
                                            step=1, 
                                            key="delete_task")
        if st.button("삭제"):
            delete_task(int(delete_task_input))
    
    st.header("현재 할 일 목록")
    view_tasks()

if __name__ == "__main__":
    main()
