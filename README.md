# Sprint_6: Тестирование  сервиса «Яндекс.Самокат».

## Содержание проекта
1. Папка pages: POM-модели для главной страницы, страницы заказов
2. Папка tests: тест-кейсы для тестирования раздела  «Вопросы о важном», создания заказа, перехода на страницу Яндекса
3. Файл .gitignore: файлы, которые не должны попасть в git
4. Файл confest: содержит функцию, которая создает драйвер
5. Файл data: данные для тест-кейсов
6. Файл README.md: описание проекта
7. Файл requirements.txt: необходимые зависимости

## Запуск проекта:
1. Создать и активировать виртуальное окружение Python
2. Установить зависомсти: pip install requirements.txt
3. Запустить тесты: pytest -v
4. После завершения тестов появится папка с отчетами allure_results

## Сборка отчетов:
1. Генерация: pytest -v --alluredir=allure_results
2. Создание html-страниц с отчетами: allure serve allure_results