let domain = 'http://127.0.0.1:8000'

function register_relocate() {
    location.href = domain + "/auth/register/";
}

function my_experiences(name) {
    let user = name.toString()
    location.href = domain + `/profiles/my_experiences/${user}`;
}

function change_password(id) {
    location.href = domain + `/profiles/change_password/${id}`;
}

function edit_profile() {
    location.href = domain + `/profiles/edit_profile/`;
}

function experiences_relocate() {
    location.href = domain + "/experience/";
}

function blog_relocate() {
    location.href = domain + "/blog/";
}

