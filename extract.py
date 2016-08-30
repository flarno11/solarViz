from bs4 import BeautifulSoup

s = '''
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>
	smart-me  - Energy Monitoring
</title><meta name="description" content="smart-me is a simple Cloud-based Energy Monitoring Solution." /><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- core CSS -->
    <link rel="stylesheet" href="Content/css/bootstrap/bootstrap.min.css" type="text/css" />
    <link rel="stylesheet" href="Content/css/bootstrap/font-awesome.min.css" type="text/css" />
    <link rel="stylesheet" href="Content/css/bootstrap/animate.min.css" type="text/css" />
    <link rel="stylesheet" href="Content/css/bootstrap/prettyPhoto.css" type="text/css" />
    <link rel="stylesheet" href="Content/css/bootstrap/main.css" type="text/css" />
    <link rel="stylesheet" href="Content/css/bootstrap/responsive.css" type="text/css" />

    <!--[if lt IE 9]>
    <script src="Scripts/bootstrap/html5shiv.js" type="text/javascript"></script>
    <script src="Scripts/bootstrap/respond.min.js" type="text/javascript"></script>
    <![endif]-->
    <link rel="shortcut icon" href="favicon.ico"/>
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="Images/icons/apple-touch-icon-144-precomposed.png"/>
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="Images/icons/apple-touch-icon-114-precomposed.png"/>
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="Images/icons/apple-touch-icon-72-precomposed.png"/>
    <link rel="apple-touch-icon-precomposed" href="Images/icons/apple-touch-icon-57-precomposed.png"/>



    <link href="/Content/css/bootstrap/SignIn.css" type="text/css" rel="stylesheet" />
</head>
 <body class="homepage">
    <form method="post" action="./SignIn.aspx?ReturnUrl=%2fDetails%2fAll.aspx" id="form1">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="NDPvsI7gUwdEg0QcCGF6QNq2dpyjoaWCtfrOkZSpA1hpG7xsUI/LAFPH9y0aUS9jQTkn7eYxQztagA6r5NwDq91Sm/g=" />

<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="ECDA716A" />
<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="kJXQmMHJJXG9SG4wLzwnc5NnDYHxNj/SjayXgrHOxggi90HSxv6kDJHHLKwydD4jQANPsOT7Gt2nMhFurBW+zTya7icbvRIcAFsBRGG8LyLiq8/uvsspMC4+qjvAKngOc80vQwdaa5SJJiay3T9q5B0Psxs=" />

         <!-- The Header -->
        <header id="header">

        <nav class="navbar navbar-inverse" role="banner">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="default.aspx"><img src="Images/bootstrap/logo.png" alt="logo"/></a>
                </div>

                <div class="collapse navbar-collapse navbar-right">
                    <ul class="nav navbar-nav">
                        <li><a href="Details/Home.aspx">Login</a></li>
                        <li><a href="Description/HowItWorks.aspx">How it works</a></li>
                         <li><a href="Description/Products.aspx">Products</a></li>
                        <li><a href="Description/Pricing.aspx">Pricing</a></li>
                         <li><a href="buy/">Buy</a></li>
						<li><a href="http://en.wiki.smart-me.com" target="_blank">Wiki</a></li>
						<li><a href="Sample/Sample.aspx">Demo</a></li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">More <i class="fa fa-angle-down"></i></a>
                            <ul class="dropdown-menu">
							<li><a href="Description/App.aspx">Apps</a></li>
                            <li><a href="Description/billing/">smart-me Billing</a></li>
							 <li><a href="support/">Support</a></li>
							 <li><a href="Developer/">Developer</a></li>
							 <li><a href="About/ContactUs.aspx">Contact</a></li>
                            </ul>
                        </li>


                    </ul>
                </div>
            </div><!--/.container-->
        </nav><!--/nav-->

    </header><!--/header-->



    <div class="container">
        <div class="row">
            <div class="col-sm-6 col-md-4 col-md-offset-4">
                <div class="account-wall">
                    <div id="my-tab-content" class="tab-content">
                        <div class="tab-pane active" id="login">
                            <img class="profile-img" src="Images/logoBlueSmall.png" alt="" />



                            <table id="ContentPlaceHolder1_Login1" cellspacing="0" cellpadding="0">
	<tr>
		<td>
                                    <p class="validation-summary-errors">

                                    </p>

                                    <input name="ctl00$ContentPlaceHolder1$Login1$UserName" type="text" id="ContentPlaceHolder1_Login1_UserName" class="form-control" autofocus="" placeholder="User name" />

                                    <input name="ctl00$ContentPlaceHolder1$Login1$Password" type="password" id="ContentPlaceHolder1_Login1_Password" class="form-control" placeholder="Password" />

                                    <input type="submit" name="ctl00$ContentPlaceHolder1$Login1$ctl01" value="Sign In" class="btn btn-lg btn-default btn-block" />

                                </td>
	</tr>
</table>

                            <br />
                            <div id="tabs" data-tabs="tabs">
                                <p class="text-center"><a href="Users/SignUp.aspx">Register as new user</a></p>
                                <p class="text-center"><a href="Users/RequestPasswordReset.aspx">Forgot password?</a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <br />


        <!--footer-->
        <footer id="footer" class="midnight-blue">
        <div class="container">
            <div class="row">
                <div class="col-sm-6">
                    &copy; 2016 <a target="_blank" href="https://smart-me.com" title="smart-me Energymonitoring">smart-me</a>
                </div>
                <div class="col-sm-6">
                    <ul class="pull-right">
                        <li><a href="About/Privacy.aspx">Data protection guidelines</a></li>
					    <li><a href="About/TermsOfService.aspx">Terms of service</a></li>
                        <li><a href="About/ContactUs.aspx">Contact</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer><!--/#footer-->

    </form>

    <script src="Scripts/jquery-1.7.1.min.js" type="text/javascript"></script>
    <script src="Scripts/bootstrap/bootstrap.min.js" type="text/javascript"></script>
    <script src="Scripts/bootstrap/jquery.prettyPhoto.js" type="text/javascript"></script>
    <script src="Scripts/bootstrap/jquery.isotope.min.js" type="text/javascript"></script>
    <script src="Scripts/bootstrap/main.js" type="text/javascript"></script>
    <script src="Scripts/bootstrap/wow.min.js" type="text/javascript"></script>

       <script type="text/javascript">

        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-39019091-1']);
        _gaq.push(['_trackPageview']);

        (function () {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
        })();

    </script>
</body>
</html>
'''

soup_mysite = BeautifulSoup(s, "html.parser")

fields = {input.get('name'): input.get('value') for input in soup_mysite.find_all("input")}

print(fields)