<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KiyoShop - modern online shop by Dmitri & T</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #4361ee;
            --secondary: #3f37c9;
            --accent: #4cc9f0;
            --dark: #1a1a2e;
            --light: #f8f9fa;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f7fa;
            background-image: radial-gradient(circle at 10% 20%, rgba(67, 97, 238, 0.1) 0%, transparent 20%), 
                            radial-gradient(circle at 90% 80%, rgba(76, 201, 240, 0.1) 0%, transparent 20%);
            color: #333;
            line-height: 1.6;
        }

        header {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            padding: 15px 0;
            color: white;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .logo {
            font-size: 28px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 15px;
            position: relative;
        }

        .logo-symbol {
            display: flex;
            align-items: center;
            position: relative;
            width: 80px;
            height: 40px;
        }

        .logo-man {
            position: absolute;
            font-size: 32px;
            color: white;
        }

        .logo-man.left {
            left: 0;
            transform: scaleX(-1);
        }

        .logo-man.right {
            right: 0;
        }

        .logo-earth {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            font-size: 24px;
            color: #64b5f6;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(-5px); }
        }

        .search-box {
            flex: 0 1 600px;
            margin: 0 20px;
            position: relative;
        }

        .search-box input {
            width: 100%;
            padding: 12px 20px;
            padding-left: 45px;
            border-radius: 30px;
            border: none;
            font-size: 16px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .search-box i {
            position: absolute;
            left: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--primary);
        }

        .user-actions {
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .user-actions a {
            color: white;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 5px;
            transition: all 0.3s ease;
            padding: 8px 12px;
            border-radius: 5px;
        }

        nav {
            background: var(--dark);
            padding: 12px 0;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 15px;
            justify-content: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        nav a {
            color: white;
            text-decoration: none;
            padding: 8px 15px;
            border-radius: 5px;
            transition: all 0.3s ease;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .content-section {
            display: none;
            animation: fadeIn 0.5s ease;
            min-height: 70vh;
        }

        .content-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .categories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin: 40px 0;
        }

        .category-card {
            background: white;
            padding: 25px;
            text-align: center;
            border-radius: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            position: relative;
            overflow: hidden;
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .product-card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            position: relative;
        }

        footer {
            background: var(--dark);
            color: white;
            padding: 40px 0;
            margin-top: 50px;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        @media (max-width: 768px) {
            .header-top {
                flex-wrap: wrap;
                gap: 15px;
            }

            .search-box {
                flex: 1 1 100%;
                order: 3;
                margin: 15px 0 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-top">
            <div class="logo">
                <div class="logo-symbol">
                    <i class="fas fa-male logo-man left"></i>
                    <i class="fas fa-globe logo-earth"></i>
                    <i class="fas fa-male logo-man right"></i>
                </div>
                KiyoShop
            </div>
            <div class="search-box">
                <i class="fas fa-search"></i>
                <input type="text" placeholder="Search products...">
            </div>
            <div class="user-actions">
                <a href="#" class="login-btn">
                    <i class="fas fa-user"></i>
                    Login
                </a>
                <a href="#" class="cart-btn">
                    <i class="fas fa-shopping-cart"></i>
                    Cart (<span id="cart-count">0</span>)
                </a>
            </div>
        </div>
    </header>

    <nav>
        <ul>
            <li><a href="#home" class="nav-link active"><i class="fas fa-home"></i> Home</a></li>
            <li><a href="#categories" class="nav-link"><i class="fas fa-list"></i> Categories</a></li>
            <li><a href="#products" class="nav-link"><i class="fas fa-box-open"></i> Products</a></li>
            <li><a href="#sales" class="nav-link"><i class="fas fa-tag"></i> Sales</a></li>
            <li><a href="#contacts" class="nav-link"><i class="fas fa-phone-alt"></i> Contacts</a></li>
        </ul>
    </nav>

    <main>
        <section id="home" class="content-section active">
            <div class="container">
                <div class="categories">
                </div>
                <div class="products-grid">
                </div>
            </div>
        </section>

        <section id="categories" class="content-section">
            <div class="container">
                <div class="categories">
                </div>
            </div>
        </section>

        <section id="products" class="content-section">
            <div class="container">
                <div class="products-grid">
                </div>
            </div>
        </section>

        <section id="contacts" class="content-section">
            <div class="container">
                <div class="footer-content">
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>© 2025 KiyoShop. All rights reserved</p>
        </div>
    </footer>

    <script>
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                document.querySelectorAll('.nav-link, .content-section').forEach(el => {
                    el.classList.remove('active');
                });
                this.classList.add('active');
                const sectionId = this.getAttribute('href').substring(1);
                document.getElementById(sectionId).classList.add('active');
            });
        });
    </script>
</body>
</html>
