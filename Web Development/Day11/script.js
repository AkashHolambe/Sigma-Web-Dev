// Function to add a new task
function addTask() {
    var taskInput = document.getElementById('taskInput');
    var taskList = document.getElementById('taskList');

    if (taskInput.value === '') {
        alert('Please enter a task.');
        return;
    }

    // Create new list item
    var li = document.createElement('li');
    li.innerHTML = taskInput.value + '<button onclick="removeTask(this)">Remove</button>';

    // Append the new task to the task list
    taskList.appendChild(li);

    // Clear the input field
    taskInput.value = '';
}

// Function to remove a task
function removeTask(button) {
    var listItem = button.parentNode;
    var taskList = listItem.parentNode;

    // Remove the task from the list
    taskList.removeChild(listItem);
}
