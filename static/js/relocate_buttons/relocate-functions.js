let domain = 'http://127.0.0.1:8000'

function register_relocate() {
    location.href = domain + "/auth/register/";
}

function my_experiences(name){
    let user = name.toString()
    location.href = domain + `/profiles/my_experiences/${user}`;
}

function change_password(id){
    location.href = domain + `/profiles/change_password/${id}`;
}

function edit_profile(){
    location.href = domain + `/profiles/edit_profile/`;
}
// {% extends 'base.html' %}
// {% load static %}
// {% block title %}
//     My Profile
// {% endblock %}
//
// {% block page_content %}
//     <header id="gtco-header" class="gtco-cover gtco-cover-md" role="banner"
//             style="background-image: url({% static 'images/veliko-tarnovo-bulgaria-community-building-travel.jpg' %})">
//         <div class="container">
//             <br><br><br><br><br>
//             <div class="main-body">
//
//                 <br>
//                 <div class="row gutters-sm">
//                     <div class="col-md-4 mb-3">
//                         <div class="card">
//                             <div class="card-body">
//                                 <div class="d-flex flex-column align-items-center text-center">
//                                     <img src="{{ profile.profile_picture.url }}" alt="Admin" class="rounded-circle"
//                                          width="150">
//                                     <div class="mt-3">
//                                         <br>
//
//                                         <a href="{% url 'my experiences' request.user %}" class="btn btn-primary">
//                                             My Experiences</a>
//
//
//                                     </div>
//                                     <div class="mt-3">
//                                         <br>
//                                         <a href="{% url 'edit profile' request.user.id %}" class="btn btn-primary">Edit Profile</a>
//                                         <a href="{% url 'change password' request.user.id %}" class="btn btn-primary">Change
//                                             Password</a>
//                                     </div>
//                                     <br>
//                                 </div>
//                             </div>
//                         </div>
//                         <div class="card mt-3">
//                             <ul class="list-group list-group-flush">
//
//                                 <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
//                                     <h6 class="mb-0">
//                                         <a href="#"><i class="icon-facebook" style="font-size: 24px"></i></a>
//                                         Facebook
//                                     </h6>
//                                     <span class="text-secondary">{{ profile.facebook_account }}</span>
//                                 </li>
//                                 <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
//                                     <h6 class="mb-0">
//                                         <a href="#"><i class="icon-instagram" style="font-size: 24px"></i></a>
//                                         Instagram
//                                     </h6>
//                                     <span class="text-secondary">{{ profile.instagram_account }}</span>
//                                 </li>
//                                 <li class="list-group-item d-flex justify-content-between align-items-center flex-wrap">
//                                     <h6 class="mb-0">
//                                         <a href="#"><i class="icon-twitter" style="font-size: 24px"></i></a>
//                                         Twitter
//                                     </h6>
//                                     <span class="text-secondary">{{ profile.twitter_account }}</span>
//                                 </li>
//                             </ul>
//                         </div>
//                     </div>
//
//                     <div class="col-md-8">
//                         <div class="card mb-3">
//                             <div class="card-body">
//                                 <div class="row">
//                                     <div class="col-sm-3">
//                                         <h6 class="mb-0">First Name</h6>
//                                     </div>
//                                     <div class="col-sm-9 text-secondary">
//                                         {{ profile.first_name }}
//                                     </div>
//                                 </div>
//                                 <hr>
//                                 <div class="row">
//                                     <div class="col-sm-3">
//                                         <h6 class="mb-0">Last Name</h6>
//                                     </div>
//                                     <div class="col-sm-9 text-secondary">
//                                         {{ profile.last_name }}
//                                     </div>
//                                 </div>
//                                 <hr>
//                                 <div class="row">
//                                     <div class="col-sm-3">
//                                         <h6 class="mb-0">Country</h6>
//                                     </div>
//                                     <div class="col-sm-9 text-secondary">
//                                         {{ profile.country }}
//                                     </div>
//                                 </div>
//                                 <hr>
//                                 <div class="row">
//                                     <div class="col-sm-3">
//                                         <h6 class="mb-0">Description</h6>
//                                     </div>
//                                     <div class="col-sm-9 text-secondary">
//                                         {{ profile.description }}
//                                     </div>
//                                 </div>
//                                 <hr>
//
//                             </div>
//                         </div>
//
//
//                     </div>
//                 </div>
//
//             </div>
//         </div>
//     </header>
//
// {% endblock %}
