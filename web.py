import streamlit as st
import functions
import os
import time

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

todos_list = functions.read_file()

enable = st.checkbox("Enable camera", key="camera_enabled")

st.camera_input(label="Take a Photo and make Video from it!",
                disabled=not enable,
                label_visibility="visible",
                key="take_photo")

picture = st.session_state["take_photo"]

if picture:
    st.image(picture)
    st.button("Make video", key="make_video", use_container_width=True)
    if st.session_state["make_video"]:
        time.sleep(3)
        del st.session_state["take_photo"]
        st.video("cat.mp4", loop=True)

# def add_todo():
#     new_todo = st.session_state["input_todo"] + '\n'
#
#     todos_list.append(new_todo)
#     functions.write_file(todos_list)
#
# st.title("TODO List")
#
# for index, todo in enumerate(todos_list):
#     checkbox = st.checkbox(todo, key=todo)
#     if checkbox:
#         todos_list.pop(index)
#         functions.write_file(todos_list)
#         del st.session_state[todo]
#         st.rerun()
#
# st.text_input(label="Enter a todo:", placeholder="Add a new todo...", label_visibility="collapsed",
#               on_change=add_todo, key="input_todo")
