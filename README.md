# homework_70_yerbol_zhulniyazov
<h1 align="center"> Issue Tracker </h1>
<p>Продолжение Проекта Issue Tracker. Добавлено приложение api, добавлены сериализаторы и выполнены следующие требования:

`Напишите DetailView, UpdateView и DeleteView для API тасктрекера, используя сериализатор с занятия и базовый класс APIView:

    DetailView должен выводить данные одного проекта и задачи методом GET.
    UpdateView должен обновлять выбранный проект и задачи методом PUT. 
    В случае успешного обновления возвращайте все её поля. В случае неуспешного - ошибки.
    DeleteView должен удалять проект и задачу методом DELETE и возвращать её ключ в ответе.`

**Добавлены новые ссылки для вышеуказанного функционала, чтобы можно было выбрать как именнно взаимодействовать 
с задачами и проектами. Пользователь может посмотреть, обновить и удалить проект или задачу использую API(новый функционал) или  Django generic views.**  
<p>Добавлены пользователи, группы и выданы права для взаимодействий с приложением.
<p>Суперпользователь:</p>
<h5>Логин: admin</h5>
<h5>Пароль: root</h5>
<p>Пользователи:</p>
<h5>Логин: manager</h5>
<h5>Пароль: manager</h5>
<h5>Логин: lead</h5>
<h5>Пароль: lead</h5>
<h5>Логин: dev</h5>
<h5>Пароль: dev</h5>
