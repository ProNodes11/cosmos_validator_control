# cosmos_validator_control
Софт для контроля работы космфорк валидаторов и отслеживания актуального баланса стейка

1) Install git; go; python3
2) Установите tenderduty:
```bash
git clone https://github.com/blockpane/tenderduty.git
cd tenderduty
go build
```
3) Скопируйте файлы из этого репозитория(важно чтобы они были в одной папке)
4) Дайте права на использование add_chain.sh (chmod +x add_chain.sh)
5) Используйте ./add_chain.sh чтобы добавить ваших валидаторов в список просматриваемых
6) Добавьте токен ТГ бота в config.yml и main.py
7) Установите screen
8) Запустите скрин для вотчера:
```bash
screen -S tenderduty
./tenderduty -f /путь/к/config.yml
CTRL+A+D
```
9) Запустите скрин для чекера балансов:
```bash
screen -S balances
python3 main.py
CTRL+A+D
```
Если хотите добавить сеть:
```bash
screen -r tenderduty
CTRL+C
./add_chain.sh
./tenderduty -f /путь/к/config.yml
CTRL+A+D
```

Почитать больше про config.yml:
https://github.com/blockpane/tenderduty/blob/main/docs/config.md
