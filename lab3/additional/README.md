# Дополнительные материалы ЛР3

Роль выгрузки NetBox, вспомогательный сценарий export.yml, настройки Ansible, скриншоты и изображения схемы.

Два обязательных сценария и выгрузка NetBox находятся на уровень выше. Для повторного запуска из папки lab3:

```bash
ANSIBLE_CONFIG=additional/ansible.cfg ansible-playbook additional/export.yml --check -e @/path/to/secrets.json
ANSIBLE_CONFIG=additional/ansible.cfg ansible-playbook configure-from-netbox.yml -e @/path/to/secrets.json
ANSIBLE_CONFIG=additional/ansible.cfg ansible-playbook collect-serials.yml -e @/path/to/secrets.json
```

Следует указать собственные данные доступа к NetBox и маршрутизаторам. Команды в отчёте сохранены в том виде, в котором выполнялись на учебном стенде.
