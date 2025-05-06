<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KiyoShop - Cosmic Experience</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #4361ee;
            --secondary: #3f37c9;
            --accent: #4cc9f0;
            --dark: #1a1a2e;
            --light: #f8f9fa;
            --cosmic-purple: #3a0ca3;
            --cosmic-blue: #480ca8;
            --cosmic-pink: #f72585;
            --cosmic-teal: #4cc9f0;
            --sale-red: #ff3860;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            color: #333;
            line-height: 1.6;
            margin: 0;
            overflow-x: hidden;
            background: linear-gradient(135deg, var(--cosmic-purple), var(--cosmic-blue));
        }

        .cosmic-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
            background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        }

        .star {
            position: absolute;
            background-color: white;
            border-radius: 50%;
            animation: burn 3s ease-out infinite;
            opacity: 0;
        }

        @keyframes burn {
            0% {
                transform: scale(0.1);
                opacity: 0;
                box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.8);
            }
            50% {
                opacity: 1;
                box-shadow: 0 0 20px 10px rgba(255, 215, 0, 0.6);
            }
            100% {
                transform: scale(1.2);
                opacity: 0;
                box-shadow: 0 0 40px 20px rgba(255, 69, 0, 0);
            }
        }

        .shooting-star {
            position: absolute;
            width: 4px;
            height: 4px;
            background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 50%, rgba(255,255,255,0) 100%);
            border-radius: 50%;
            animation: shooting 3s linear infinite;
            opacity: 0;
        }

        @keyframes shooting {
            0% {
                transform: translateX(0) translateY(0);
                opacity: 1;
            }
            70% {
                opacity: 1;
            }
            100% {
                transform: translateX(1000px) translateY(300px);
                opacity: 0;
            }
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
            background: rgba(255,255,255,0.9);
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
            background: rgba(255,255,255,0.1);
        }

        nav {
            background: var(--dark);
            padding: 12px 0;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 60px;
            z-index: 99;
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
            background: rgba(255,255,255,0.1);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 2;
        }

        .content-section {
            display: none;
            animation: fadeIn 0.5s ease;
            min-height: 70vh;
            background: rgba(255,255,255,0.9);
            border-radius: 15px;
            margin: 20px 0;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        .content-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
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
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
        }

        .btn {
            display: inline-block;
            padding: 12px 30px;
            background: var(--primary);
            color: white;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
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
    <style>
        
        footer {
            background: var(--dark);
            color: white;
            padding: 40px 0 20px;
            margin-top: 50px;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .footer-column {
            padding: 15px;
        }

        .footer-column h4 {
            color: var(--cosmic-teal);
            margin-bottom: 20px;
            font-size: 1.2em;
        }

        .footer-column ul {
            list-style: none;
            padding: 0;
        }

        .footer-column ul li {
            margin-bottom: 10px;
        }

        .footer-column a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-column a:hover {
            color: var(--cosmic-teal);
        }

        .copyright {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }

        
        nav ul {
            gap: 10px;
            flex-wrap: wrap;
        }

        
        @media (max-width: 768px) {
            .footer-content {
                grid-template-columns: 1fr;
            }
        
        footer {
            background: var(--dark);
            color: white;
            padding: 40px 0 20px;
            margin-top: auto;
            position: relative;
            z-index: 2;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .footer-column {
            padding: 15px;
        }

        .footer-column h4 {
            color: var(--cosmic-teal);
            margin-bottom: 20px;
            font-size: 1.2em;
        }

        .footer-column ul {
            list-style: none;
            padding: 0;
        }

        .footer-column ul li {
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .footer-column a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-column a:hover {
            color: var(--cosmic-teal);
        }

        .copyright {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }

        .social-links a {
            font-size: 1.5em;
            margin-right: 15px;
            color: white;
            transition: color 0.3s ease;
        }

        .social-links a:hover {
            color: var(--cosmic-teal);
        }

        .payment-methods i {
            font-size: 2em;
            margin-right: 10px;
        }

        @media (max-width: 768px) {
            .footer-content {
                grid-template-columns: 1fr;
                text-align: center;
            }
            
            .footer-column ul li {
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <div class="cosmic-background" id="cosmicBackground"></div>
    
    <div class="content-wrapper">
        <header>
            <div class="header-top">
                <div class="logo">
                    <span class="logo-symbol">
                        <span class="logo-man left">🧑‍🚀</span>
                        <span class="logo-earth">🌍</span>
                        <span class="logo-man right">🧑‍🚀</span>
                    </span>
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
            </ul>
       </nav>


        <main>
            <section id="home" class="content-section active">
                <div class="container">
                    <div class="hero">
                        <h1>Welcome to KiyoShop</h1>
                        <p>Experience shopping like never before!</p>
                        <button class="btn">Explore our Universe!</button>
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

    <footer>
        <div class="container">
            <div class="footer-content">
                 <div class="footer-column">
                    <h4>About KiyoShop</h4>
                    <p>Exploring the universe of shopping since 2025. We bring you the best products from across the world with lightning-fast delivery!</p>
                    <div class="social-links" style="margin-top: 15px;">
                        <a href="#"><i class="fab fa-facebook"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                
                <div class="footer-column">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="#home">Home</a></li>
                        <li><a href="#products">Products</a></li>
                        <li><a href="#sales">Sales</a></li>
                        <li><a href="#contacts">Support</a></li>
                    </ul>
                </div>

                <div class="footer-column">
                    <h4>Contacts</h4>
                    <ul>
                        <li><i class="fas fa-map-marker-alt"></i> Vienna</li>
                        <li><i class="fas fa-phone"></i> + 777777777</li>
                        <li><i class="fas fa-envelope"></i> support@kiyoshop.space</li>
                    </ul>
                    <div class="payment-methods" style="margin-top: 20px;">
                        <i class="fab fa-cc-visa" style="font-size: 2em; margin-right: 10px;"></i>
                        <i class="fab fa-cc-mastercard" style="font-size: 2em; margin-right: 10px;"></i>
                        <i class="fab fa-cc-paypal" style="font-size: 2em;"></i>
                    </div>
                </div>
            </div>
            <div class="copyright">
                <p>© 2025 KiyoShop. All rights reserved</p>
            </div>
        </div>
    </footer>
</div>

<script>
    function createCosmicBackground() {
            const cosmicBackground = document.getElementById('cosmicBackground');
            
            for(let i = 0; i < 100; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                star.style.left = `${Math.random() * 100}%`;
                star.style.top = `${Math.random() * 100}%`;
                star.style.animationDelay = `${Math.random() * 3}s`;
                cosmicBackground.appendChild(star);
            }

            setInterval(() => {
                const shootingStar = document.createElement('div');
                shootingStar.className = 'shooting-star';
                shootingStar.style.left = `${Math.random() * 20}%`;
                shootingStar.style.top = `${Math.random() * 20}%`;
                cosmicBackground.appendChild(shootingStar);
                
                setTimeout(() => shootingStar.remove(), 3000);
            }, 5000);
        }

  
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

        
        createCosmicBackground();
</script>
</body>
</html>