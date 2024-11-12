import streamlit as st
import functions
import os

if not os.path.exists("tasks.txt"):
    with open('tasks.txt', 'w') as file:
        pass
    

def add_task():
    task = st.session_state['new_task'] + '\n'  #refers to the task in the input box
    #print(task)
    tasks.append(task)
    functions.write_tasks(tasks)
    st.session_state.new_task = text_input
    if 'new_task' == '' or 'new_task' == ' ':
        return


def complete_task(key):
    num = int(key)
    st.write(f'This task "{tasks.pop(num)}')
    functions.write_tasks(tasks)

#retrieve the task list in tasks.txt - to be displayed
tasks = functions.get_tasks()

st.title('My Task App')

st.subheader('This is my Tasks Web App.')
#st.subheader('Hello Burg! Thanks for checking! :*')

st.write('This app is to increase you productivity.')

for index, task in enumerate(tasks[1:], start=1):
    checkbox = st.checkbox(task.capitalize(), key=index,
                        on_change=complete_task, args=(str(index)))
    # if checkbox:
    #     #print(checkbox)
    #     tasks.pop(index)
    #     functions.write_tasks(tasks)
    #     del st.session_state[task]
    #     st.experimental_rerun() #This method did not exist in version 1.40.0 of Streamlit.

text_input = st.text_input(label='', placeholder="Add a new task...",
                        disabled=False,
                        on_change=add_task, key='new_task', 
                        help="Type a new to-do and press Enter to add it to the list")

# print('Hello')
# st.session_state

