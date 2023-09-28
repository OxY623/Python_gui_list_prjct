# Python_gui_list_prjct
Десктопная программа по добавлению и удалению списка.

Далее инструкция по установке: 
Скачайте проект с репозитория GitHub. Для этого перейдите на страницу проекта на GitHub и нажмите на кнопку "Code" (или "Код"). Выберите опцию "Download ZIP" (или "Скачать ZIP") для загрузки проекта в виде ZIP-архива.

Если вы предпочитаете использовать Git, скопируйте URL репозитория и выполните команду git clone <URL> в командной строке.

Разархивируйте ZIP-архив, если вы скачали проект в виде ZIP. В результате вы получите папку с проектом.

Установите виртуальную среду Python. Создание и активация виртуальной среды помогут изолировать зависимости проекта от других установленных пакетов.

Для создания виртуальной среды можно использовать venv. Откройте командную строку (терминал) и перейдите в папку проекта. Затем выполните следующую команду:

python -m venv .venv
Это создаст виртуальную среду с именем ".venv".

Активируйте виртуальную среду:

Для Windows:
  .venv\Scripts\activate
Для macOS и Linux:
  source .venv/bin/activate
Установите зависимости проекта. В папке проекта выполните следующую команду, чтобы установить все необходимые пакеты:

pip install -r requirements.txt

Теперь вы можете запустить проект. В командной строке перейдите в папку проекта и выполните команду:
  py main.py