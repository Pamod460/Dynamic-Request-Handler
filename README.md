## Dynamic Request Handler

A custom ERPNext application for handling dynamic requests. This app extends ERPNext functionality with custom request handling capabilities.

### Installation

#### Stable (main branch)

1. Fetch the app from GitHub into your local Frappe bench:
```bash
bench get-app dynamic_request_handler https://github.com/Pamod460/Dynamic-Request-Handler.git
```

2. Install the app on your specific ERPNext site:
```bash
bench --site [your-site-name] install-app dynamic_request_handler
```
*(Replace `[your-site-name]` with the actual name of your site, e.g., `site1.local`)*

#### Development branch

1. Fetch the app from the `Development` branch:
```bash
bench get-app dynamic_request_handler https://github.com/Pamod460/Dynamic-Request-Handler.git --branch Development
```

2. Install the app on your site:
```bash
bench --site [your-site-name] install-app dynamic_request_handler
```

### Uninstallation

If you need to remove the app later, follow these steps:

1. Uninstall the app from your ERPNext site:
```bash
bench --site [your-site-name] uninstall-app dynamic_request_handler
```

2. Remove the app completely from your Frappe bench:
```bash
bench remove-app dynamic_request_handler
```

### Requirements

- ERPNext 14.x or higher
- Python 3.10+
- Frappe Framework

### Features

- Dynamic request handling
- Custom API endpoints
- Request processing and management

### Development

Install in development mode:
```bash
bench install-app --with-dev-dependencies dynamic-request-handler
```

### Contributing

Contributions are welcome! Please feel free to submit pull requests.

### Support

For issues and questions, please create an issue on GitHub.

#### License

MIT