<div align="center" markdown="1">
<img src="https://user-images.githubusercontent.com/46772424/181754239-a337beb3-fd35-4f27-969c-b9793f011458.svg" alt="Helpdesk logo" width="170"/>

**Open Source Helpdesk** </br>
[helpdesk.com](https://helpdesk.com)

</div>

---

Frappe Helpdesk offers an easy setup, clean user interface, and automation tools to resolve customer issues efficiently. It is based on Frappe Framework. It lets you streamline your company's support and helps you to efficiently manage your customer queries. It can help you to,

-   Create tickets from email or help center
-   Empower customers with a comprehensive knowledge base and self-service portal
-   Automate redundant tasks like agent assignment and set up triggers to notify agents and customers based on certain events

<img src="https://user-images.githubusercontent.com/46772424/180410739-a64b8b65-43b4-4ec8-8a87-1f5e97f355e0.png" width=" ">

## Installation

### Local

To setup the repository locally follow the steps mentioned below:

1. Install bench and setup a `frappe-bench` directory by following the [Installation Steps](https://frappeframework.com/docs/user/en/installation)
1. Start the server by running `bench start`
1. In a separate terminal window, create a new site by running `bench new-site helpdesk.test`
1. Map your site to localhost with the command `bench --site helpdesk.test add-to-hosts`
1. Get the Frappe Helpdesk app. Run `bench get-app https://github.com/frappe/desk`
1. Run `bench --site helpdesk.test install-app helpdesk`.
1. Now open the URL `http://helpdesk.test:8000/helpdesk` in your browser, you should see the app running

## Contributions and Community

There are many ways you can contribute even if you don't code:

1. You can start by giving a star to this repository!
2. If you find any issues, even if it is a typo, you can [raise an issue](https://github.com/frappe/desk/issues/new) to inform us.
3. You can join our [telegram group](https://t.me/helpdesk) and share your thoughts.

## License

[GNU Affero General Public License v3.0](https://github.com/frappe/desk/blob/main/licence.md)
