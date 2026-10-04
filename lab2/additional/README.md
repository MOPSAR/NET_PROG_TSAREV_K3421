# Дополнительные материалы ЛР2

Сценарии Ansible, inventory, журналы и скриншоты. Обязательные конфигурации CHR1.rsc и CHR2.rsc находятся на уровень выше.

Для повторного запуска следует перейти в эту папку и указать свой файл с переменными доступа:

```bash
ansible-playbook configure.yml -e @/path/to/secrets.json
ansible-playbook collect.yml -e @/path/to/secrets.json
```
