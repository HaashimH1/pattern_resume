# Pattern Resume

Resume Template Marketplace is an innovative e-commerce platform built with Django that empowers you to purchase and personalize professionally designed resume templates. With seamless Stripe payment integration and secure authentication via django-allauth (including Google sign-in), our website offers a streamlined experience that transforms the way you present your career story. Whether you're revamping your resume or starting anew, our marketplace provides a wide selection of modern templates designed to help you stand out in today’s competitive job market.

Live site can be found [Here](https://pattern-resume-9bdbd99a82a6.herokuapp.com/)

---

## Table of Contents

- [Introduction](#introduction)
  - [Objective](#objective)
  - [Audience](#audience)
- [Business and Marketing Plan](#business-and-marketing-plan)
  - [Business Objectives](#business-objectives)
  - [User Experience (UX) Strategy](#user-experience-ux-strategy)
  - [Target Market](#target-market)
  - [Revenue Model](#revenue-model)
  - [Marketing Strategy](#marketing-strategy)
  - [Growth Opportunities](#growth-opportunities)
  - [Digital Marketing Mockups](#digital-marketing-mockups)
- [Design](#design)
  - [Mockups](#mockups)
  - [Rationale](#rationale)
- [Agile Approach and Project Management](#agile-approach-and-project-management)
- [Role-Based Authorization](#role-based-authorization)
- [Models Overview](#models-overview)
- [Manual Testing Table](#manual-testing-table)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Introduction

### Objective
Create a robust platform for selling resume templates that users can easily customize through an intuitive design, secure e-commerce flow, and dynamic content management.

### Audience
- **Job Seekers:** Professionals at all career stages looking to enhance their resumes.
- **Recent Graduates:** Individuals entering the job market who need a polished, professional resume.
- **Freelancers and Contractors:** Independent professionals seeking flexible, high-quality resume templates.
- **Career Advisors:** Coaches and recruiters who wish to offer modern, customizable resume solutions.

---

## Business and Marketing Plan

### Business Objectives
- **Seamless E-Commerce Experience:** Provide a smooth, modern platform for purchasing and customizing resume templates.
- **Diverse Template Portfolio:** Offer a wide range of contemporary, industry-specific designs.
- **Secure Transactions:** Integrate Stripe for payment processing and django-allauth for robust user authentication.
- **User-Friendly Customization:** Enable effortless template customization.
- **Scalable Infrastructure:** Ensure the platform scales with increasing user demand and regular template updates.

### User Experience (UX) Strategy
- **Intuitive Navigation:** Clear, responsive menus with breadcrumb trails.
- **Real-Time Feedback:** Custom notifications and AJAX interactions for immediate feedback.
- **Accessible Design:** Implement clear instructions, robust error handling, ARIA roles, and keyboard navigation.
- **Mobile-First Approach:** Optimize the design for mobile devices.
- **Visual Impact:** Use modern aesthetics and high-quality visuals to showcase resume templates.

### Target Market
- **Primary:** Job seekers and professionals looking to update or create standout resumes.
- **Secondary:** Recent graduates entering the job market.
- **Tertiary:** Career advisors, HR professionals, and recruitment agencies seeking quality resume solutions.

### Revenue Model
- **Template Sales:** One-time purchases for individual resume templates.

### Marketing Strategy
- **SEO:** Use targeted keywords, unique meta tags, structured data, canonical URLs, and an XML sitemap to improve search rankings.
- **Social Media:** Leverage a dedicated Facebook Business Page (see Digital Marketing Mockups) to build brand awareness.
- **Email Marketing:** Use Mailchimp for regular newsletters and lead magnets.
- **Paid Advertising & Partnerships:** Run targeted ad campaigns and collaborate with career coaches and HR platforms.
- **Content & Community Engagement:** Maintain a blog with resume tips and success stories to build trust.

### Growth Opportunities
- **Expanded Template Library:** Continuously add new, industry-specific templates.
- **Interactive Customization Tools:** Develop in-browser editors for real-time resume customization.
- **User Reviews & Ratings:** Implement a review system for social proof and ongoing improvement.
- **Mobile Application:** Develop a native mobile app for on-the-go resume creation.
- **Advanced Analytics:** Leverage data analytics to optimize the user experience.
- **Strategic Partnerships:** Collaborate with job boards, career coaches, and HR service providers to expand market reach.

### Digital Marketing Mockups

To illustrate our digital marketing strategy, we created an in-house mockup of a Facebook Business Page. This controlled approach ensures full brand consistency and minimizes risks associated with live social media accounts during early development.

#### Facebook Business Page Mockup Details
- **Cover Photo:**  
  A high-resolution image featuring our resume templates in a sleek, modern workspace, conveying quality and innovation.
- **Profile Picture:**  
  Our brand logo, designed with clean lines and a modern aesthetic, ensures immediate recognition.
- **About Section:**  
  A concise overview of our mission:  
  *"Empowering professionals to enhance their career prospects through customizable, high-quality resume templates."*  
  This section details our services and provides contact information.
- **Content Strategy:**  
  - **Educational Posts:** Regular updates with resume tips, industry insights, and career advice.
  - **Promotional Posts:** Announcements for new templates, special offers, and subscription benefits.
  - **Interactive Content:** Live Q&A sessions, polls, and video testimonials.
- **Call-to-Actions (CTAs):**  
  Strategically placed CTAs such as "Shop Now," "Customize Your Resume," and "Learn More" drive traffic to our marketplace.

**Justification:**  
We chose to use a mockup instead of a live Facebook Business Page to maintain full control over our brand image during development. This approach avoids risks like policy violations or account suspension and ensures that our digital marketing materials reflect our intended brand identity accurately.

---

## Design

![Colour palette used in website: white, teal, and gold](/README_assets/doc_1.png)
- **White:** Background color for a clean, minimalist look.
- **Teal and Yellow:** Provide contrast to highlight key elements.

### Mockups

#### Home Mock
![Home page design mockup](/README_assets/doc_wf_1.png)
- A hero section introduces the platform.
- Prominent login/register buttons are featured.
- Key features are clearly highlighted.

#### Login/Register Mock
![Login page design mockup](/README_assets/doc_wf_2.png)
- Google sign-in is integrated for streamlined authentication.
- Forms for username, email, and password are provided, with clear validation messages.

#### Dashboard Mock
![Dashboard design mockup](/README_assets/doc_wf_3.png)
- **Editor (left):** Area for managing resume data.
- **Preview (right):** Real-time preview of the resume.
- The layout is fully responsive, stacking vertically on smaller screens.

### Rationale
- **Simplicity & Minimalism:** Emphasis on essential actions with minimal distractions.
- **Mobile-First Design:** Optimized for mobile usability using flexbox and media queries.
- **Consistent Navigation:** Uniform navigation and footer across pages for familiarity.
- **User Feedback:** Clear visual cues and error messages enhance user interaction.

---

## Agile Approach and Project Management

Our project was developed using agile methodologies, divided into four sprints:

### Sprint 1: Setup & Authentication
- **Objectives:**  
  Establish the Django project structure and integrate django-allauth (with Google sign-in) for secure user registration and login.
- **Process:**  
  Detailed GitHub issues were created for tasks like "Implement user registration" and "Integrate Google authentication."
- **Outcome:**  
  A secure authentication system with robust error handling and user feedback.

### Sprint 2: Dashboard Implementation
- **Objectives:**  
  Develop an interactive dashboard for managing resume templates and customizations.
- **Process:**  
  GitHub issues focused on "Create Dashboard layout" and "Implement CRUD operations for resume data."
- **Outcome:**  
  A dynamic dashboard that enables efficient resume management.

### Sprint 3: Payment Integration
- **Objectives:**  
  Integrate Stripe for secure payment processing and develop a reliable checkout workflow.
- **Process:**  
  Tasks such as "Set up Stripe Checkout Session" and "Handle Stripe webhook events" were iteratively developed and tested.
- **Outcome:**  
  A seamless payment process with clear transaction feedback.

### Sprint 4: Styling and Responsiveness
- **Objectives:**  
  Finalize the front-end design to ensure a modern, responsive, and accessible UI.
- **Process:**  
  Issues like "Responsive design adjustments" and "Implement custom toasts for user feedback" were addressed via code reviews and user feedback.
- **Outcome:**  
  A polished design that meets accessibility standards and provides a smooth user experience.

### Continuous Improvement and Collaboration
- **GitHub Integration:**  
  Used for task management, sprint planning, and code reviews.
- **Team Communication:**  
  Daily stand-ups and sprint retrospectives ensured rapid issue resolution and iterative improvements.

---

## Role-Based Authorization

To safeguard sensitive operations, Pattern Resume implements role-based authorization using Django’s permission framework, custom decorators, and middleware—integrated with django-allauth (including Google sign-in).

### How It Works

- **User Roles and Permissions:**
  - **Standard Users:** Can browse, purchase templates, customize resumes, and view order history.
  - **Admin Users:** Marked by Django’s `is_staff` attribute; have access to administrative functions such as template management and order processing.
  - Permissions are enforced using Django’s built-in system, ensuring each role can only perform its authorized actions.

- **Custom Decorators:**
  - Decorators (e.g., `@user_is_admin`) restrict access to sensitive views.
  - Example:
    ```python
    from django.http import HttpResponseForbidden
    from functools import wraps

    def user_is_admin(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.is_staff:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    ```

- **Middleware Integration:**
  - Custom middleware checks user sessions and permissions before processing requests, blocking unauthorized access early in the request cycle.

- **Protected Views:**
  - Critical functions—such as template purchases, resume customization, and order management—are secured using these methods.

### Benefits
- **Enhanced Security:** Sensitive operations are protected from unauthorized access.
- **Seamless Social Authentication:** Integration with django-allauth (including Google sign-in) ensures secure onboarding.
- **Granular Access Control:** Only users with appropriate roles can access certain features.
- **Scalability:** The framework can be easily extended to accommodate additional roles or permissions.

---

## Models Overview

### UserStatus

| **Field**       | **Type**                                   | **Purpose/Description**                                                                                       |
|-----------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| user            | OneToOneField (settings.AUTH_USER_MODEL)   | Associates each user with a unique status record, ensuring every user has one related status instance.          |
| has_purchased   | BooleanField (default=False)               | Indicates whether the user has made a purchase.                                                               |
| templates       | ManyToManyField ('Template', blank=True)   | Maintains a list of resume templates that the user has purchased.                                             |

**Purpose:**  
Stores the purchase status and the collection of owned resume templates for each user.

### Template

| **Field**    | **Type**                     | **Purpose/Description**                                                                                                  |
|--------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| name         | CharField (max_length=255)   | The title or name of the resume template.                                                                              |
| price        | DecimalField (max_digits=6, decimal_places=2) | The cost associated with purchasing the template.                                                                      |
| description  | TextField                    | A detailed description of the template, highlighting its features and benefits.                                         |
| html_content | TextField                    | The HTML markup used to render the resume template.                                                                    |
| css_content  | TextField                    | The CSS styles applied for visual formatting.                                                                           |
| img_url      | TextField                    | A URL pointing to an image preview of the template, used for display on product pages.                                   |

**Purpose:**  
Holds all essential details for each resume template available for purchase, including content and styling.

### Order

| **Field**         | **Type**                                              | **Purpose/Description**                                                                                          |
|-------------------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| user              | ForeignKey (settings.AUTH_USER_MODEL)                | References the user who made the purchase.                                                                       |
| template          | ForeignKey (Template)                                 | Identifies the purchased resume template.                                                                        |
| stripe_charge_id  | CharField (max_length=255)                            | Stores the unique identifier returned by Stripe for the payment transaction.                                     |
| amount            | DecimalField (max_digits=6, decimal_places=2)         | The amount charged for the purchase.                                                                             |
| created_at        | DateTimeField (auto_now_add=True)                     | The timestamp when the order was created.                                                                        |

**Purpose:**  
Tracks each purchase transaction and records payment details.

### Resume

| **Field**     | **Type**                                                | **Purpose/Description**                                                                                   |
|---------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| user          | ForeignKey (settings.AUTH_USER_MODEL, related_name='resumes') | Associates the resume with the user who created it.                                                      |
| template      | ForeignKey (Template, on_delete=SET_NULL, null=True)     | References the resume template used to generate the resume.                                               |
| summary       | TextField                                               | A brief personal summary or profile statement for the resume.                                            |
| first_name    | CharField (max_length=30, default="First name")          | The first name of the resume owner.                                                                       |
| last_name     | CharField (max_length=30, default="Last name")           | The last name of the resume owner.                                                                        |
| job_title     | CharField (max_length=30, default="Job title")           | The professional title or position of the resume owner.                                                  |
| email         | TextField (default="Email Address")                     | The email address of the resume owner.                                                                    |
| phone_number  | CharField (max_length=20, default="Phone number")        | The contact phone number for the resume owner.                                                            |
| city          | CharField (max_length=30, default="City")                | The city where the resume owner is located.                                                               |
| last_saved    | DateTimeField (auto_now=True)                           | Timestamp of the last update made to the resume.                                                          |

**Purpose:**  
Represents the resume data for each user, including personal details and content to be rendered using the purchased template.

### ResumeSection

| **Field**  | **Type**                                           | **Purpose/Description**                                                                                     |
|------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| resume     | ForeignKey (Resume, related_name='sections')       | Links the section to a specific resume.                                                                     |
| name       | CharField (max_length=30)                          | The title of the resume section (e.g., "Experience", "Education").                                           |
| order      | PositiveIntegerField (default=1)                   | Specifies the display order of the section within the resume.                                               |

**Purpose:**  
Organizes the resume into logical sections to control content sequencing.

### ResumeSubSection

| **Field**   | **Type**                                           | **Purpose/Description**                                                                                     |
|-------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| section     | ForeignKey (ResumeSection, related_name='sub')     | Associates the sub-section with its parent resume section.                                                |
| title       | CharField (max_length=60)                          | The title or heading for the sub-section (e.g., "Software Engineer at TechCorp").                           |
| description | TextField                                          | Detailed information or description for the sub-section.                                                  |
| order       | PositiveIntegerField (default=1)                   | Determines the display order of the sub-section within the parent section.                                  |

**Purpose:**  
Allows for a granular breakdown of resume content by organizing detailed entries (such as job roles or educational achievements) within each section.

---

## E-Commerce Business Model and Marketing Strategies

### Overview and Requirements
Our application is designed with a B2C focus—targeting individual professionals and job seekers who need high-quality, customizable resume templates. The core business intent is to provide a seamless, secure, and engaging platform that empowers users to purchase and personalize resume templates, thereby enhancing their professional image and career opportunities.

### Business Model
- **Product Offering:**  
  A diverse collection of professionally designed resume templates that are fully customizable and optimized for high-quality PDF conversion.
- **Revenue Streams:**  
  - **One-Time Purchases:** Purchase individual resume templates.
  - **Subscription Services:** Premium plans offering exclusive access to new templates and additional customization features.
  - **Customization Packages:** Bespoke resume editing and design adjustments.
- **Secure Transactions:**  
  Integration with Stripe ensures secure payment processing, while django-allauth (with Google sign-in) provides robust user authentication.
- **User Engagement:**  
  A user-friendly dashboard allows customers to manage purchased templates, customize their resumes, and download final products.
- **Purpose Focus (B2C):**  
  Tailored for individual professionals and job seekers looking to enhance their resumes.

### Marketing Strategies
- **SEO:**  
  Utilize targeted keywords, unique meta tags, structured data, canonical URLs, and an XML sitemap to boost organic search rankings.
- **Social Media:**  
  Leverage a dedicated Facebook Business Page, using our in-house mockup (detailed below) to build brand awareness.
- **Email Marketing:**  
  Implement regular newsletter campaigns with Mailchimp and lead magnets such as free resume guides.
- **Paid Advertising & Partnerships:**  
  Run targeted ad campaigns and collaborate with career coaches and HR platforms.
- **Content & Community Engagement:**  
  Maintain a blog and resource center featuring resume tips and success stories, along with user testimonials to build trust.

### Digital Marketing Mockups

To illustrate our digital marketing strategy, we designed an in-house mockup of a Facebook Business Page. This mockup was created to maintain full control over our brand presentation and to mitigate risks associated with using a live social media account during the development phase.

#### Facebook Business Page Mockup Details
- **Cover Photo:**  
  A high-resolution image showcasing our resume templates in a sleek, modern workspace that conveys quality and innovation.
- **Profile Picture:**  
  Our brand logo, designed with clean lines and a modern aesthetic, ensuring immediate brand recognition.
- **About Section:**  
  A concise overview of Pattern Resume’s mission:  
  *"Empowering professionals to enhance their career prospects through customizable, high-quality resume templates."*  
  This section details our services and includes transparent contact information.
- **Content Strategy:**  
  - **Educational Posts:** Regular updates offering resume tips, industry insights, and career advice.
  - **Promotional Posts:** Announcements for new template launches, special offers, and subscription benefits.
  - **Interactive Content:** Engagement through live Q&A sessions, polls, and video testimonials.
- **Call-to-Actions (CTAs):**  
  Strategically placed CTAs like "Shop Now," "Customize Your Resume," and "Learn More" drive traffic directly to our marketplace.

**Justification:**  
Using a mockup instead of a live Facebook Business Page allows us to maintain complete control over our brand image during early development, avoiding risks such as policy violations or account suspension. This ensures our digital marketing materials accurately reflect our envisioned brand identity.

---

## Manual Testing Table

| **Feature**                   | **Test Description**                                                                                   | **Expected Outcome**                                                                                               | **Result** |
|-------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|------------|
| **Navigation**                | Ensure all navigation links (Home, Templates, Dashboard, Login, Register, Logout) are functional.       | Each link redirects correctly, with the navigation menu consistently displayed.                                    | PASS       |
| **Register**                  | Test registration with valid inputs.                                                                   | User account is created and redirected with a success message.                                                     | PASS       |
|                               | Test registration with invalid inputs.                                                                 | Appropriate error messages are displayed; registration is blocked until corrections are made.                        | PASS       |
| **Login**                     | Test login with valid credentials.                                                                     | User logs in and is redirected to the Dashboard with all account details loaded.                                    | PASS       |
|                               | Test login with invalid credentials.                                                                   | An error message is displayed, and the user remains on the login page.                                               | PASS       |
| **Logout**                    | Test logout functionality.                                                                             | User is logged out, the session is terminated, and the user is redirected to the Home Page.                            | PASS       |
| **Dashboard**                 | Verify the Dashboard displays purchased templates, customized resume data, and order history accurately. | Dashboard loads user-specific data with clear options to manage, edit, and preview resumes.                           | PASS       |
| **Template Purchase**         | Test purchasing a resume template using valid payment details via Stripe.                              | Payment is processed, the template is added to the user's account, and a confirmation message is displayed.             | PASS       |
|                               | Test purchasing with invalid payment details.                                                        | Payment is declined with a clear error message prompting valid details.                                               | PASS       |
| **Resume Customization**      | Test editing and saving a resume using a purchased template.                                           | Changes are saved and immediately reflected in the resume preview; PDF generation functions correctly.                | PASS       |
| **Feedback & Error Handling** | Validate that forms provide real-time feedback and display error messages appropriately.                 | Error messages trigger for invalid or missing inputs, guiding the user to correct them before proceeding.                | PASS       |
| **Responsive Design**         | Test the site on various devices to verify layout and functionality.                                   | The interface adapts correctly across devices with all elements accessible and well-aligned.                            | PASS       |
| **Session Management**        | Test session persistence by logging in, closing the browser, and reopening it.                         | The user remains logged in if the session is active; otherwise, they are prompted to log in again.                       | PASS       |
| **Database Integration**      | Test CRUD operations on user resumes and template orders.                                             | Data is stored, retrieved, updated, and deleted correctly with immediate reflection on the UI.                          | PASS       |
| **API Integration**           | Test API calls for payment processing and template data retrieval.                                     | API responses are handled correctly; relevant data is displayed without errors.                                         | PASS       |
| **Accessibility**             | Test site navigation using keyboard-only interactions (tab, enter).                                    | All interactive elements are accessible via keyboard with visible focus indicators.                                   | PASS       |
| **Deployment**                | Verify that the live site is accessible via the deployed URL and loads all resources correctly.          | The website is live, fully functional, and performs consistently under real-world conditions.                           | PASS       |

---

## Technologies Used

### Languages and Frameworks
- **Python:** Primary language for backend logic, API integrations, and business rules.
- **Django:** Manages models, views, URL routing, and template rendering.
- **HTML:** Structures the web page content.
- **CSS:** Styles the user interface and ensures responsiveness.
- **JavaScript (with jQuery):** Adds client-side interactivity and dynamic behavior.

### Development Tools
- **Visual Studio Code (via GitPod):** IDE used for coding, debugging, and testing.
- **Git:** Version control system for managing code changes.
- **GitHub:** Repository hosting for code review, issue tracking, and continuous integration.

### Deployment
- **Heroku:** Cloud hosting platform for deploying the live version of the application.
- **Gunicorn:** WSGI HTTP server used on Heroku for efficient request handling.

---

## Deployment

This section details the process to deploy the Resume Template Marketplace on Heroku. Follow these steps to replicate the deployment process:

### **Hosting Platform**
The project is hosted on **Heroku**, which simplifies Django deployment. GitHub is used for continuous deployment.

### **Steps to Deploy on Heroku**

1. **Create a Heroku Account**
   - Sign up at [Heroku's website](https://www.heroku.com/).

2. **Install the Heroku CLI**
   - Download and install the CLI from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

3. **Prepare the Django Project**
   - Update `requirements.txt`:
     ```bash
     pip freeze > requirements.txt
     ```
   - Create a `Procfile` in the root directory:
     ```plaintext
     web: gunicorn my_project.wsgi
     ```
   - In `settings.py`, set:
     ```python
     ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com']
     ```

4. **Initialize a New Heroku App**
   - Log in via the CLI:
     ```bash
     heroku login -i
     ```
   - Create the app:
     ```bash
     heroku create your-heroku-app-name
     ```

5. **Configure Environment Variables on Heroku**
   - Set the required variables:
     ```bash
     heroku config:set DEBUG=False
     heroku config:set SECRET_KEY='your-secret-key'
     heroku config:set DATABASE_URL='your-database-url'
     ```
   - Add any additional variables (e.g., API keys, Stripe credentials).

6. **Connect to Your GitHub Repository**
   - In the Heroku dashboard, navigate to "Deploy".
   - Select "GitHub" as the deployment method.
   - Connect your repository and enable automatic deploys from the main branch.

7. **Deploy the Application**
   - Click "Deploy Branch" and monitor the logs for errors.

8. **Verify the Deployment**
   - Visit:
     ```plaintext
     https://your-heroku-app-name.herokuapp.com
     ```
   - Ensure all features (registration, payment, resume customization) are working.

---

### **Cloning the Repository Locally**

1. **Clone the Repository**
   - Run:
     ```bash
     git clone https://github.com/your-username/your-repository-name.git
     ```

2. **Set Up a Virtual Environment**
   - Navigate to the project directory:
     ```bash
     python -m venv venv
     ```
   - Activate the environment:
     ```bash
     # Windows:
     venv\Scripts\activate
     # macOS/Linux:
     source venv/bin/activate
     ```

3. **Install Dependencies**
   - Run:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Application Locally**
   - Migrate and start the server:
     ```bash
     python manage.py migrate
     python manage.py runserver
     ```
   - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

### **PostgreSQL Integration**
- For production, PostgreSQL is provisioned automatically by Heroku.
- The `DATABASES` setting in `settings.py` is configured using the `DATABASE_URL` environment variable.
- Verify that this setup is correctly configured on Heroku.

---

### **Final Verification**
After deployment, ensure:
- All navigation links function correctly.
- User authentication (registration, login, logout) works seamlessly.
- Purchasing and customization of resume templates function as expected.
- The design is responsive across devices.
- All resources (static files, images, etc.) load properly and quickly.

By following these steps, you can deploy and maintain the Resume Template Marketplace successfully on Heroku or a similar hosting platform.

---

## Credits

- Most images used were generated from text descriptions with [DALL-E Open-AI](https://openai.com/index/dall-e-3/)
- Font is from [Google Fonts](https://fonts.google.com/)
- Feature implementation guidance provided using [Chat GPT](https://openai.com/index/chatgpt/)
- Icons sourced from [Flaticon](https://www.flaticon.com/)
- Free HTML to PDF API available from [here](https://pdf-api.co/docs/)
- Newsletter powered by [Mailchimp](https://mailchimp.com/)
- Dashboard design inspired by [resume.io](https://resume.io/)
- Project setup guided by resources from [Code Institute](https://codeinstitute.net/)
