function create_a_new_task() {
    const createTaskButton = $('#create-task-btn');
    createTaskButton.click(() => {
        const newTaskContainer = $('<form>', { id: 'new-task-container' });

        // Create input fields and append them to the new task container
        const taskTitle = $('<input>', { id: 'task-title', name: 'title', type: 'text', placeholder: 'Task Title', required: true });
        const taskDescription = $('<textarea>', { id: 'task-description', name: 'description', placeholder: 'Task Description', required: true });
        const taskDueDate = $('<input>', { id: 'task-due-date', name: 'due_date', type: 'date', required: true });
        const addTaskButton = $('<button>', { id: 'add-task-btn', text: 'Create Task', type: 'submit' });

        newTaskContainer.append(taskTitle);
        newTaskContainer.append(taskDescription);
        newTaskContainer.append(taskDueDate);
        newTaskContainer.append(addTaskButton);

        $('#body-container').append(newTaskContainer);

        newTaskContainer.hide().slideDown();

        // Handle form submission
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
                    // Optionally, you can clear the form or update the task list
                    newTaskContainer[0].reset();
                },
                error: function(error) {
                    alert('Error creating task: ' + error.responseText);
                }
            });
        });
    });
}

function show_task_list() {
    // Implementation for showing the task list
}

document.addEventListener('DOMContentLoaded', () => {
    create_a_new_task();
});
