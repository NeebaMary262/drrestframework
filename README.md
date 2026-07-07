#  Django REST Framework: Mixins & Generics CRUD API

A foundational backend service demonstrating clean, DRY (Don't Repeat Yourself) API architecture using Django REST Framework's advanced class-based views.

This project implements full CRUD (Create, Read, Update, Delete) functionality by leveraging DRF's built-in Mixins and Generic API Views, significantly reducing boilerplate code while maintaining scalability.

##  Key Features
* **Full CRUD Operations:** Seamless handling of GET, POST, PUT, PATCH, and DELETE requests.
* **Class-Based Architecture:** Replaces bulky function-based views with streamlined `GenericAPIView` implementations.
* **Mixin Integration:** Uses `CreateModelMixin`, `ListModelMixin`, `RetrieveModelMixin`, `UpdateModelMixin`, and `DestroyModelMixin` for modular endpoint behavior.
* **Serialization:** Robust data validation and conversion between complex querysets and JSON data.

##  Tech Stack
* **Language:** Python
* **Web Framework:** Django
* **API Toolkit:** Django REST Framework (DRF)
* **Database:** SQLite (Default, scalable to PostgreSQL)

##  How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <YOUR-GITHUB-REPO-LINK-HERE>
   cd drrestframework