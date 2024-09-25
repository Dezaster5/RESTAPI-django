from django.http import HttpResponse
from django.urls import reverse

def home(request):
    return HttpResponse(f"""
        <h1>Добро пожаловать в API для управления объектами Item</h1>
        <p>Вот доступные URL-адреса и действия:</p>
        <ul>
            <li><a href="{reverse('schema-swagger-ui')}">Swagger UI</a> — Документация API (Swagger)</li>
            <li><a href="{reverse('schema-redoc')}">ReDoc UI</a> — Документация API (ReDoc)</li>
            <li><a href="/api/items/">/api/items/</a> — Получить список всех предметов (GET)</li>
            <li><a href="/admin/">/admin/</a> — Панель администратора Django</li>
        </ul>
        <p>Используйте соответствующие HTTP методы для работы с объектами Item:</p>
        <ul>
            <li><strong>POST</strong> для создания нового предмета</li>
            <li><strong>GET</strong> для получения списка всех предметов или одного предмета по ID</li>
            <li><strong>PUT/PATCH</strong> для обновления предмета</li>
            <li><strong>DELETE</strong> для удаления предмета</li>
        </ul>
    """)