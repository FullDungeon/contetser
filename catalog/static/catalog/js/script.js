function clickTopic(topic_id) {
    let element = document.getElementById(this.id);
    
    let topicList = element.closest(".topic__list");
    let topicListClasses = topicList.classList;

    if (topicListClasses.contains("topic__list--selected")) {
        topicListClasses.remove("topic__list--selected");

        let taskList = topicList.querySelector('.task__list');
        taskList.style.display = 'none';
        taskList.style.maxHeight = '';
    }
    else {
        topicListClasses.add("topic__list--selected");

        let taskList = topicList.querySelector('.task__list');
        taskList.style.display = 'flex';
        taskList.style.flexDirection = 'column';
        taskList.style.maxHeight = '100%';
    }

}

let allTopics = document.querySelectorAll(".topic");

for (let i = 0; i < allTopics.length; i++) {
    allTopics[i].addEventListener("click", clickTopic);
}

