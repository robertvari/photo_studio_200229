let menu_display = false;

function menu_clicked() {
    let logo_element = document.getElementById("logo");
    let submenu_layout = document.getElementById("submenu_layout");
    let category_menu = document.getElementById("category_menu");

    if(menu_display){
        logo_element.style.display = "none";
        submenu_layout.style.display = "none";

        // move category menu to original position
        category_menu.style.top = "40px";

        menu_display = false

    }else{
        logo_element.style.display = "block";
        submenu_layout.style.display = "flex";

        // offset category menu
        category_menu.style.top = "150px";

        menu_display = true
    }


}