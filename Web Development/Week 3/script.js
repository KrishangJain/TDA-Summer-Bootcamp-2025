let input = document.getElementById("taskInput");
let button = document.getElementById("addButton");
let list = document.getElementById("taskList");
let tasks = [];

if (localStorage.getItem("myTasks")) {
  tasks = JSON.parse(localStorage.getItem("myTasks"));
  showTasks();
}

button.onclick = function () {
  let text = input.value;
  if (text === "") return;
  let task = { text: text, done: false };
  tasks.push(task);
  input.value = "";
  saveAndShow();
};

function showTasks() {
  list.innerHTML = "";
  tasks.forEach((task, index) => {
    let item = document.createElement("li");
    let span = document.createElement("span");
    span.innerText = task.text;
    if (task.done) span.classList.add("done");
    span.onclick = function () {
      tasks[index].done = !tasks[index].done;
      saveAndShow();
    };
    let removeButton = document.createElement("button");
    removeButton.innerText = "Delete";
    removeButton.onclick = function () {
      tasks.splice(index, 1);
      saveAndShow();
    };
    item.appendChild(span);
    item.appendChild(removeButton);
    list.appendChild(item);
  });
}

function saveAndShow() {
  localStorage.setItem("myTasks", JSON.stringify(tasks));
  showTasks();
}