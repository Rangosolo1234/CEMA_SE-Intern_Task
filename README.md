# GeoHIS – Geospatial Health Information System

![GeoHIS Banner](your-image-path.jpg)

## Overview

**GeoHIS** is a robust, modern Health Information System (HIS) built with Django and advanced GIS (Geographic Information System) capabilities. It empowers organizations to manage, visualize, and analyze health data spatially, enabling smarter healthcare decisions and resource allocation.

GeoHIS combines the power of **Django**, **PostGIS**, and **Leaflet** to deliver a scalable, secure, and extensible platform for healthcare data management, spatial analytics, and RESTful API integrations.

---

## ✨ Features

- **Spatial Data Management:** Store, query, and visualize geographic health data (hospitals, clients, incidences, etc.) using PostGIS and GeoDjango.
- **RESTful API:** Robust, flexible API powered by Django REST Framework and DRF-GIS, supporting GeoJSON for spatial data.
- **Interactive Maps:** Seamless Leaflet integration for dynamic, real-time map visualizations.
- **Modular Architecture:** Clean separation of concerns with reusable Django apps and serializers.
- **Secure & Extensible:** Ready for production with best practices for security, authentication, and environment management.
- **Admin Interface:** Powerful Django admin for managing all health data models.

---

## 🚀 Quick Start

### 1. **Clone the Repository**



### 2. **Set Up a Virtual Environment**


### 3. **Install Requirements**



### 4. **Configure Environment Variables**

Create a `.env` file in the root directory:



### 6. **Run the Development Server**



### 7. **Access the API**

Visit [http://localhost:8000/api/](http://localhost:8000/api/) to explore the API endpoints.

---

## 🗺️ Core Architecture

- **Django 5.2** with GeoDjango for spatial data support.
- **PostgreSQL + PostGIS** for advanced GIS queries.
- **Django REST Framework** and **djangorestframework-gis** for RESTful, spatially-enabled APIs.
- **Leaflet.js** for interactive mapping on the frontend.
- **CORS** and **CSRF** securely configured for modern web apps.

---

## 📦 Main Apps & Models

- **Hospitals:** Location-aware hospital management.
- **Health Programs:** Program tracking and analytics.
- **Doctor Profiles:** Professional and spatial data for doctors.
- **Clients:** Patient records with geolocation.
- **Bookings:** Scheduling and visit management.
- **Blog Posts:** Health news and updates.
- **Incidences:** Spatial incident reporting and visualization.

---

## 🔒 Security & Best Practices

- **Environment Variables:** All sensitive data and keys are managed via `.env`.
- **Authentication:** Ready for JWT, token, or session-based authentication.
- **CORS:** Configured for safe cross-origin requests.
- **Production Ready:** Disable debug, secure secret keys, and use HTTPS in production.

---

## 🧩 Requirements

All dependencies are listed in `requirements.txt`. Key packages include:

- `Django==5.2`
- `djangorestframework==3.16.0`
- `djangorestframework-gis==1.1`
- `django-leaflet==0.31.0`
- `django-cors-headers==4.7.0`
- `psycopg2==2.9.10`
- `GDAL` (ensure correct version and path for your OS)
- See full list in [requirements.txt](requirements.txt)

---

## 🛠️ Development & Contribution

1. Fork the repository and create your feature branch.
2. Write clean, well-documented code and tests.
3. Submit a pull request with a clear description.

---

## 📚 Documentation & Resources

- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostGIS Documentation](https://postgis.net/documentation/)
- [Leaflet.js](https://leafletjs.com/)
- [DRF-GIS](https://github.com/openwisp/django-rest-framework-gis)

---

## 💡 Screenshots
![clientsapi](https://github.com/user-attachments/assets/614f5917-775f-4aa2-8844-334b19fdbc8a)


---

## 📬 Contact

For questions, suggestions, or contributions, open an issue or contact [your-email@example.com](mailto:your-email@example.com).

---

> **GeoHIS** – Empowering smarter, spatially-driven healthcare decisions!
