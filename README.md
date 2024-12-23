# DJCLI - Django Command Line Interface

**DJCLI** is a simple tool to streamline common Django management tasks. Instead of typing verbose `python manage.py` commands, you can use intuitive shorthand commands like `djcli migrate` or `djcli runserver`.

---

## Features
- Simplifies Django management commands.
- Customizable command aliases.
- Lightweight and easy to set up.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/vince13/djcliv1.git
cd djcliv1
```

### 2. Make the Script Executable
Add a shebang to the script if not already included:
```python
#!/usr/bin/env python3
```

Change file permissions to make it executable:
```bash
chmod +x djcli.py
```

### 3. Add to Your PATH (Optional for Global Use)
To use `djcli` as a global command, copy it to a directory in your `PATH`:
```bash
sudo cp djcli.py /usr/local/bin/djcliv1
```

Verify it works:
```bash
djcli_github --help
```

---

## Usage
Navigate to a Django project directory (where `manage.py` is located) and use the following commands:

### Available Commands
| Shorthand Command       | Equivalent Django Command                       |
|--------------------------|------------------------------------------------|
| `djcli runserver`       | `python manage.py runserver`                   |
| `djcli migrate`         | `python manage.py migrate`                     |
| `djcli makemigrations`  | `python manage.py makemigrations`              |
| `djcli createsuperuser` | `python manage.py createsuperuser`             |
| `djcli shell`           | `python manage.py shell`                       |

### Examples
1. Start the development server:
   ```bash
   djcli runserver
   ```

2. Apply migrations:
   ```bash
   djcli migrate
   ```

3. Create a superuser:
   ```bash
   djcli createsuperuser
   ```

4. Enter the Django shell:
   ```bash
   djcli shell
   ```

---

## Customization
The command aliases can be customized by modifying the `COMMAND_MAP` in `djcli.py`:
```python
COMMAND_MAP = {
    "runserver": ["python", "manage.py", "runserver"],
    "migrate": ["python", "manage.py", "migrate"],
    "makemigrations": ["python", "manage.py", "makemigrations"],
    "createsuperuser": ["python", "manage.py", "createsuperuser"],
    "shell": ["python", "manage.py", "shell"],
}
```

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
Special thanks to the open-source community for inspiration and support.

---

### Notes
For detailed Django usage and management commands, refer to the [Django Documentation](https://docs.djangoproject.com).
