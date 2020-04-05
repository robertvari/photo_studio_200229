let menu_display = false;

function menu_clicked() {
    let logo_element = document.getElementById("logo");
    let submenu_layout = document.getElementById("submenu_layout");

    if(menu_display){
        logo_element.style.display = "none";
        submenu_layout.style.display = "none";
        menu_display = false

    }else{

        logo_element.style.display = "block";
        submenu_layout.style.display = "flex";
        menu_display = true
    }


}