function create_a_new_task() {
    const createTaskButton = $('#create-task-btn');
    
    createTaskButton.click(() => {
        let newTaskContainer = $('#new-task-container');

        if (newTaskContainer.length) {
            newTaskContainer.slideToggle();
        } else {
            newTaskContainer = $('<form>', { id: 'new-task-container' });

            const taskTitle = $('<input>', { class: "input", id: 'task-title', name: 'title', type: 'text', placeholder: 'Task Title', required: true });
            const taskDescription = $('<input>', { class: "input", id: 'task-description', name: 'description', placeholder: 'Task Description', required: true });
            const taskDueDate = $('<input>', { class: "input", id: 'task-due-date', name: 'due_date', type: 'date', required: true });
            const addTaskButton = $('<button>', { id: 'add-task-btn', text: 'Create Task', type: 'submit' });
            const refreshNote = $('<p>', { text: 'Please refresh the page to see the newly created task' });
            newTaskContainer.append(taskTitle);
            newTaskContainer.append(taskDescription);
            newTaskContainer.append(taskDueDate);
            newTaskContainer.append(addTaskButton);
            newTaskContainer.append(refreshNote);

            $('#task-form-container').append(newTaskContainer);

            newTaskContainer.hide().slideDown();

            newTaskContainer.submit(function(event) {
                event.preventDefault(); // Prevent the default form submission

                const formData = {
                    taskTitle: $('#task-title').val(),
                    taskDescription: $('#task-description').val(),
                    taskDueDate: $('#task-due-date').val()
                };

                $.ajax({
                    type: 'POST',
                    url: '/task-manager/create-task', // Adjust the URL to your backend endpoint
                    data: JSON.stringify(formData),
                    contentType: 'application/json',
                    success: function(response) {
                        alert('Task created successfully!');
                        newTaskContainer[0].reset();
                    },
                    error: function(error) {
                        alert('Error creating task: ' + error.responseText);
                    }
                });
            });
        }
    });
}

function show_task_list() {
    // Implementation for showing the task list
}

document.addEventListener('DOMContentLoaded', () => {
    create_a_new_task();
});
