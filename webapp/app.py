from flask import Flask, request, redirect, url_for, render_template_string
import json
from pathlib import Path

app = Flask(__name__)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

FILES = {
    "services": DATA_DIR / "services.json",
    "programs": DATA_DIR / "programs.json",
    "customers": DATA_DIR / "customers.json",
    "inquiries": DATA_DIR / "inquiries.json"
}


def load_data(name):
    file = FILES[name]

    if not file.exists():
        file.write_text("[]", encoding="utf-8")

    try:
        return json.loads(file.read_text(encoding="utf-8"))
    except:
        return []


def save_data(name, data):
    FILES[name].write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )


def next_id(data):
    if not data:
        return 1
    return max(item["id"] for item in data) + 1


STYLE = """
<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f4f7fb;
    color: #172033;
}

header {
    background: #102a43;
    color: white;
    padding: 18px 6%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.logo {
    font-size: 24px;
    font-weight: bold;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 8px;
    font-size: 14px;
}

nav a:hover {
    text-decoration: underline;
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: 30px auto;
}

.hero {
    background: linear-gradient(135deg, #1769aa, #102a43);
    color: white;
    padding: 45px;
    border-radius: 18px;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 38px;
    margin: 5px 0 10px;
}

.hero p {
    font-size: 17px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 5px 20px #00000012;
}

.card h3 {
    margin: 0;
    color: #667085;
}

.card strong {
    display: block;
    font-size: 32px;
    margin-top: 10px;
    color: #1769aa;
}

.panel {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 5px 20px #00000012;
    margin-bottom: 25px;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

input, select, textarea {
    width: 100%;
    padding: 12px;
    margin: 7px 0;
    border: 1px solid #ccd5e0;
    border-radius: 8px;
    font-size: 14px;
}

textarea {
    min-height: 90px;
}

button, .button {
    display: inline-block;
    background: #1769aa;
    color: white;
    border: none;
    padding: 11px 18px;
    border-radius: 8px;
    text-decoration: none;
    cursor: pointer;
    margin-top: 8px;
}

button:hover, .button:hover {
    background: #0d4f80;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    padding: 13px;
    border-bottom: 1px solid #e6eaf0;
    text-align: left;
}

th {
    background: #f1f5f9;
}

.badge {
    background: #e7f1fb;
    color: #1769aa;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
}

.success {
    background: #e8f7ed;
    color: #17663a;
    padding: 12px;
    border-radius: 8px;
    margin-bottom: 20px;
}

footer {
    text-align: center;
    padding: 25px;
    color: #667085;
}

@media(max-width:800px) {
    .cards {
        grid-template-columns: 1fr 1fr;
    }

    .grid {
        grid-template-columns: 1fr;
    }

    header {
        gap: 15px;
    }
}

@media(max-width:500px) {
    .cards {
        grid-template-columns: 1fr;
    }

    nav a {
        display: inline-block;
        margin: 5px;
    }
}
</style>
"""


BASE = """
<!DOCTYPE html>
<html>
<head>
    <title>VEDA Technology Management System</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    """ + STYLE + """
</head>

<body>

<header>

<div class="logo">
    VEDA TECHNOLOGY
</div>

<nav>
    <a href="/">Dashboard</a>
    <a href="/services">Services</a>
    <a href="/programs">Programs</a>
    <a href="/customers">Customers</a>
    <a href="/inquiries">Inquiries</a>
    <a href="/reports">Reports</a>
</nav>

</header>

<div class="container">

{{CONTENT}}

</div>

<footer>
VEDA Technology Management System | Python Flask Project
</footer>

</body>
</html>
"""


def page(content):
    return render_template_string(
        BASE.replace("{{CONTENT}}", content)
    )


@app.route("/")
def dashboard():

    services = load_data("services")
    programs = load_data("programs")
    customers = load_data("customers")
    inquiries = load_data("inquiries")

    content = f"""
    <div class="hero">
        <h1>VEDA Technology Management System</h1>
        <p>
        Manage technology services, programs, customers,
        inquiries and business reports from one platform.
        </p>
    </div>

    <div class="cards">

        <div class="card">
            <h3>Services</h3>
            <strong>{len(services)}</strong>
        </div>

        <div class="card">
            <h3>Programs</h3>
            <strong>{len(programs)}</strong>
        </div>

        <div class="card">
            <h3>Customers</h3>
            <strong>{len(customers)}</strong>
        </div>

        <div class="card">
            <h3>Inquiries</h3>
            <strong>{len(inquiries)}</strong>
        </div>

    </div>

    <div class="panel">

        <h2>Quick Actions</h2>

        <a class="button" href="/services">
            Manage Services
        </a>

        <a class="button" href="/programs">
            Manage Programs
        </a>

        <a class="button" href="/customers">
            Manage Customers
        </a>

        <a class="button" href="/inquiries">
            Service Inquiries
        </a>

        <a class="button" href="/reports">
            Business Reports
        </a>

    </div>
    """

    return page(content)


@app.route("/services", methods=["GET", "POST"])
def services():

    data = load_data("services")
    message = ""

    if request.method == "POST":

        item = {
            "id": next_id(data),
            "name": request.form["name"],
            "category": request.form["category"],
            "description": request.form["description"],
            "price": float(request.form["price"]),
            "status": request.form["status"]
        }

        data.append(item)
        save_data("services", data)

        message = "Service added successfully."

    search = request.args.get("search", "").lower()

    if search:
        data = [
            x for x in data
            if search in x["name"].lower()
            or search in x["category"].lower()
            or search in x["status"].lower()
        ]

    rows = ""

    for x in data:
        rows += f"""
        <tr>
            <td>{x['id']}</td>
            <td>{x['name']}</td>
            <td>{x['category']}</td>
            <td>₹{x['price']:,.2f}</td>
            <td><span class="badge">{x['status']}</span></td>
        </tr>
        """

    content = f"""

    <h1>Service Management</h1>

    {f'<div class="success">{message}</div>' if message else ''}

    <div class="grid">

    <div class="panel">

        <h2>Add Service</h2>

        <form method="POST">

            <input name="name"
                   placeholder="Service name"
                   required>

            <input name="category"
                   placeholder="Category"
                   required>

            <textarea name="description"
                      placeholder="Description"
                      required></textarea>

            <input name="price"
                   type="number"
                   placeholder="Estimated price"
                   required>

            <select name="status">
                <option>Active</option>
                <option>Inactive</option>
            </select>

            <button type="submit">
                Add Service
            </button>

        </form>

    </div>

    <div class="panel">

        <h2>Search Services</h2>

        <form method="GET">

            <input name="search"
                   placeholder="Search services..."
                   value="{search}">

            <button>
                Search
            </button>

        </form>

    </div>

    </div>

    <div class="panel">

    <h2>All Services</h2>

    <table>

    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Category</th>
        <th>Price</th>
        <th>Status</th>
    </tr>

    {rows}

    </table>

    </div>
    """

    return page(content)


@app.route("/programs", methods=["GET", "POST"])
def programs():

    data = load_data("programs")
    message = ""

    if request.method == "POST":

        item = {
            "id": next_id(data),
            "name": request.form["name"],
            "category": request.form["category"],
            "duration": request.form["duration"],
            "fee": float(request.form["fee"]),
            "status": request.form["status"]
        }

        data.append(item)
        save_data("programs", data)

        message = "Program added successfully."

    search = request.args.get("search", "").lower()

    if search:
        data = [
            x for x in data
            if search in x["name"].lower()
            or search in x["category"].lower()
            or search in x["status"].lower()
        ]

    rows = ""

    for x in data:
        rows += f"""
        <tr>
            <td>{x['id']}</td>
            <td>{x['name']}</td>
            <td>{x['category']}</td>
            <td>{x['duration']}</td>
            <td>₹{x['fee']:,.2f}</td>
            <td><span class="badge">{x['status']}</span></td>
        </tr>
        """

    content = f"""

    <h1>Program Management</h1>

    {f'<div class="success">{message}</div>' if message else ''}

    <div class="grid">

    <div class="panel">

    <h2>Add Program</h2>

    <form method="POST">

        <input name="name"
               placeholder="Program name"
               required>

        <input name="category"
               placeholder="Category"
               required>

        <input name="duration"
               placeholder="Duration"
               required>

        <input name="fee"
               type="number"
               placeholder="Program fee"
               required>

        <select name="status">
            <option>Open</option>
            <option>Upcoming</option>
            <option>Closed</option>
        </select>

        <button>Add Program</button>

    </form>

    </div>

    <div class="panel">

    <h2>Search Programs</h2>

    <form method="GET">

        <input name="search"
               placeholder="Search programs..."
               value="{search}">

        <button>Search</button>

    </form>

    </div>

    </div>

    <div class="panel">

    <h2>All Programs</h2>

    <table>

    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Category</th>
        <th>Duration</th>
        <th>Fee</th>
        <th>Status</th>
    </tr>

    {rows}

    </table>

    </div>

    """

    return page(content)


@app.route("/customers", methods=["GET", "POST"])
def customers():

    data = load_data("customers")
    message = ""

    if request.method == "POST":

        item = {
            "id": next_id(data),
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "organization": request.form["organization"]
        }

        data.append(item)
        save_data("customers", data)

        message = "Customer added successfully."

    search = request.args.get("search", "").lower()

    if search:

        data = [
            x for x in data
            if search in x["name"].lower()
            or search in x["email"].lower()
            or search in x["organization"].lower()
        ]

    rows = ""

    for x in data:

        rows += f"""
        <tr>
            <td>{x['id']}</td>
            <td>{x['name']}</td>
            <td>{x['email']}</td>
            <td>{x['phone']}</td>
            <td>{x['organization']}</td>
        </tr>
        """

    content = f"""

    <h1>Customer Management</h1>

    {f'<div class="success">{message}</div>' if message else ''}

    <div class="grid">

    <div class="panel">

    <h2>Add Customer</h2>

    <form method="POST">

        <input name="name"
               placeholder="Customer name"
               required>

        <input name="email"
               type="email"
               placeholder="Email"
               required>

        <input name="phone"
               placeholder="Phone"
               required>

        <input name="organization"
               placeholder="Organization"
               required>

        <button>Add Customer</button>

    </form>

    </div>

    <div class="panel">

    <h2>Search Customers</h2>

    <form method="GET">

        <input name="search"
               placeholder="Search customers..."
               value="{search}">

        <button>Search</button>

    </form>

    </div>

    </div>

    <div class="panel">

    <h2>All Customers</h2>

    <table>

    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Organization</th>
    </tr>

    {rows}

    </table>

    </div>

    """

    return page(content)


@app.route("/inquiries", methods=["GET", "POST"])
def inquiries():

    data = load_data("inquiries")
    message = ""

    if request.method == "POST":

        item = {
            "id": next_id(data),
            "customer_name": request.form["customer_name"],
            "service": request.form["service"],
            "category": request.form["category"],
            "message": request.form["message"],
            "status": "New"
        }

        data.append(item)
        save_data("inquiries", data)

        message = "Service inquiry submitted successfully."

    search = request.args.get("search", "").lower()

    if search:

        data = [
            x for x in data
            if search in x["customer_name"].lower()
            or search in x["service"].lower()
            or search in x["category"].lower()
            or search in x["status"].lower()
        ]

    rows = ""

    for x in data:

        rows += f"""

        <tr>

            <td>{x['id']}</td>

            <td>{x['customer_name']}</td>

            <td>{x['service']}</td>

            <td>{x['category']}</td>

            <td>
                <span class="badge">
                    {x['status']}
                </span>
            </td>

            <td>

                <form method="POST"
                      action="/inquiries/{x['id']}/status">

                    <select name="status">

                        <option {"selected" if x['status']=="New" else ""}>
                            New
                        </option>

                        <option {"selected" if x['status']=="In Progress" else ""}>
                            In Progress
                        </option>

                        <option {"selected" if x['status']=="Resolved" else ""}>
                            Resolved
                        </option>

                        <option {"selected" if x['status']=="Closed" else ""}>
                            Closed
                        </option>

                    </select>

                    <button>
                        Update
                    </button>

                </form>

            </td>

        </tr>

        """

    content = f"""

    <h1>Service Inquiry Management</h1>

    {f'<div class="success">{message}</div>' if message else ''}

    <div class="grid">

    <div class="panel">

    <h2>Submit Inquiry</h2>

    <form method="POST">

        <input name="customer_name"
               placeholder="Customer name"
               required>

        <input name="service"
               placeholder="Requested service"
               required>

        <input name="category"
               placeholder="Inquiry category"
               required>

        <textarea name="message"
                  placeholder="Inquiry message"
                  required></textarea>

        <button>
            Submit Inquiry
        </button>

    </form>

    </div>

    <div class="panel">

    <h2>Search Inquiries</h2>

    <form method="GET">

        <input name="search"
               placeholder="Search inquiries..."
               value="{search}">

        <button>Search</button>

    </form>

    </div>

    </div>

    <div class="panel">

    <h2>All Inquiries</h2>

    <table>

    <tr>
        <th>ID</th>
        <th>Customer</th>
        <th>Service</th>
        <th>Category</th>
        <th>Status</th>
        <th>Update</th>
    </tr>

    {rows}

    </table>

    </div>

    """

    return page(content)


@app.post("/inquiries/<int:item_id>/status")
def update_status(item_id):

    data = load_data("inquiries")

    for item in data:

        if item["id"] == item_id:

            item["status"] = request.form["status"]

            break

    save_data("inquiries", data)

    return redirect(url_for("inquiries"))


@app.route("/reports")
def reports():

    services = load_data("services")
    programs = load_data("programs")
    customers = load_data("customers")
    inquiries = load_data("inquiries")

    service_value = sum(x["price"] for x in services)
    program_value = sum(x["fee"] for x in programs)

    new_inquiries = sum(
        x["status"] == "New"
        for x in inquiries
    )

    resolved = sum(
        x["status"] == "Resolved"
        for x in inquiries
    )

    content = f"""

    <h1>Business Reports</h1>

    <div class="cards">

        <div class="card">
            <h3>Total Services</h3>
            <strong>{len(services)}</strong>
        </div>

        <div class="card">
            <h3>Total Programs</h3>
            <strong>{len(programs)}</strong>
        </div>

        <div class="card">
            <h3>Total Customers</h3>
            <strong>{len(customers)}</strong>
        </div>

        <div class="card">
            <h3>Total Inquiries</h3>
            <strong>{len(inquiries)}</strong>
        </div>

    </div>

    <div class="grid">

    <div class="panel">

        <h2>Service Summary</h2>

        <p>
            Total service value:
            <strong>₹{service_value:,.2f}</strong>
        </p>

        <p>
            Active services:
            <strong>
            {sum(x['status']=="Active" for x in services)}
            </strong>
        </p>

    </div>

    <div class="panel">

        <h2>Program Summary</h2>

        <p>
            Total program fees:
            <strong>₹{program_value:,.2f}</strong>
        </p>

        <p>
            Open programs:
            <strong>
            {sum(x['status']=="Open" for x in programs)}
            </strong>
        </p>

    </div>

    <div class="panel">

        <h2>Inquiry Summary</h2>

        <p>New inquiries: <strong>{new_inquiries}</strong></p>

        <p>Resolved inquiries: <strong>{resolved}</strong></p>

    </div>

    <div class="panel">

        <h2>Data Storage</h2>

        <p>
        Application data is stored locally
        using JSON files.
        </p>

    </div>

    </div>

    """

    return page(content)


if __name__ == "__main__":
    app.run(debug=True)
