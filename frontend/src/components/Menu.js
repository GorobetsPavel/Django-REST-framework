import React from "react";

const Menu = () => {
  return (

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <button class="navbar-toggler" type="button" data-toggle="collapse"
                        data-target="#navbarSupportedContent"
                        aria-controls="navbarSupportedContent" aria-expanded="false"
                        aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="#">"News"</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">"Courses"</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="ddProfile"
                               role="button" data-toggle="dropdown" aria-haspopup="true"
                               aria-expanded="false">
                                "Profile"
                            </a>
                            <div class="dropdown-menu" aria-labelledby="ddProfile">
                                <a class="dropdown-item"href="#">
                                    "Edit profile"
                                </a>
                                <a class="dropdown-item" href="#">"My courses"</a>
                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item" href="#">"Moderation"</a>

                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item" href="#">"Logout"</a>
                            </div>
                        </li>
                        <li class="nav-item {% if request.resolver_match.view_name == 'mainapp:contacts' %}active{% endif %}">
                            <a class="nav-link" href="#">"Contacts"</a>
                        </li>
                    </ul>

                </div>
            </div>
        </nav>

  );
};
export default Menu;