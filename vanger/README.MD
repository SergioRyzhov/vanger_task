# NASA Image Gallery

This project is a Django-based web application showcasing a gallery of images from NASA(or any other images you like). Users can view, navigate, and zoom into the images using a slick carousel and a Fancybox lightbox for a better viewing experience. The gallery images can be managed through the Django admin interface with drag-and-drop sorting functionality.

## Features

- Image gallery with slick carousel for sliding and navigating through images.
- Lightbox functionality using Fancybox for zooming into images.
- Admin interface for uploading, managing, and sorting images.
- Responsive design using Bootstrap.
- Customizable image captions and preview.

## Technologies Used

- Python 3.9
- Django
- Django Filer
- Django Admin Sortable2
- Bootstrap 5
- Slick Carousel
- Fancybox
- Docker
- Docker Compose

## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Docker
- Docker Compose

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/nasa-image-gallery.git
    cd nasa-image-gallery
    ```

2. **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

3. **Apply migrations:**

    Open a new terminal and run:

    ```bash
    docker-compose exec -it web python manage.py migrate
    ```

4. **Create a superuser:**

    ```bash
    docker-compose exec -it web python manage.py createsuperuser
    ```

5. **Access the application:**

    - Home page: `http://127.0.0.1:8000/`
    - Admin interface: `http://127.0.0.1:8000/admin/`

## Usage

### Adding Images

1. Log in to the Django admin interface at `http://127.0.0.1:8000/admin/`.
2. Use the "Images" section to upload new images.
3. Drag and drop to reorder images within the admin panel.

### Viewing Images

1. Visit the home page of the application.
2. Navigate through the images using the slick carousel.
3. Click on any image to open it in a zoomable lightbox powered by Fancybox.

## Directory Structure
```
nasa-image-gallery/
│
├── homepage/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── templates/
│ │ └── homepage/
│ │ └── index.html
│ ├── static/
│ │ └── homepage/
│ │ ├── css/
│ │ │ └── styles.css
│ │ ├── img/
│ │ │ ├── advant.jpg
│ │ │ └── space.jpeg
│ │ └── svg/
│ │ └── logo.svg
│ ├── urls.py
│ └── views.py
│
├── manage.py
├── req.pip
└── README.md
```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.