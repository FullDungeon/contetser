from django.http.response import HttpResponse
from django.template import loader

from .models import Task, Topic

# классы, представляющие собой обертки над классами Css: theme, topic и task. Нужны, чтобы в шаблон я, помимо текстового содержимого, передавал еще какие-то данные, например id. А так же, чтобы была связь между элементами в шаблоне и конкретными объектами из базы данных. Может быть это делается как-то иначе, но я не знаю как, пока что
class ThemeView:
    text = ""

    def __key__(self):
        return self.text

    def __hash__(self):
        return hash(self.text)

    def __eq__(self, other):
        if isinstance(other, ThemeView):
            return self.__key__() == other.__key__()

        return NotImplemented

class TopicView:
    btn_id = ""

    def __key__(self):
        return self.text

    def __hash__(self):
        return hash(self.text)

    def __eq__(self, other):
        if isinstance(other, TopicView):
            return self.__key__() == other.__key__()

        return NotImplemented

class TaskView:
    text = ""
    task_id = 0


# открытие страницы с каталогом задач
def catalog(request):

    # словарь словарей списков: <тема><топик> = <список задач>
    contentList = {}

    # перебор объектов из базы данных
    for element in Task.objects.all():
        # классы-обертки
        theme = ThemeView()
        topic = TopicView()
        task  = TaskView()

        theme.text   = element.topic.theme.name

        topic.text   = element.topic.name
        topic.btn_id = "topic_" + str(element.pk)

        task.text    = element.__str__()
        task.task_id = element.pk

        # наполнение словаря
        if theme in contentList:
            if topic not in contentList[theme]:
                contentList[theme].update({topic: []})
        else:
            contentList.update({theme: {topic: []}})

        contentList[theme][topic].append(task)
        

    # загрузка шаблона страницы
    template = loader.get_template('catalog/catalog.html')

    context = {
        "site_name":       "Contester 0.1",
        "page_title":      "Каталог задач",
        'contentList':      contentList,
    }

    return HttpResponse(template.render(context))


    