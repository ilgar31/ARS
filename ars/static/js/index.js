var mobile = 2
var web = 4

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value


document.getElementById("web_more").addEventListener('click', e=> {
    $.ajax({
        type: "POST",
        url: "/",
        data: {
            "csrfmiddlewaretoken": csrf,
            'from': web,
            "type": "web",
        },
        success: (res)=> {
            web = web + 4
            res.objects.forEach(i=> {
                    document.getElementById("web_projects_items").innerHTML +=  `
                        <div class="project">
                            <img src=${i.image} class="project_img">
                            <div class="project_data">
                                <div class="project_info" style="float: left;">
                                    <p class="project_name">${i.name}</p>
                                    <img src=${res.foto1} class="city_png"><p class="project_city">${i.city}</p>
                                    <img src=${res.foto2} class="floor_png"><p class="project_floor">${i.floor}</p>
                                </div>
                                <div style="float: right; font-family: Inter, sans-serif; margin-top: 20px;">
                                    <a href=${i.url} class="project_page">перейти к объекту</a><img src=${res.foto3}>
                                </div>
                            </div>
                        </div>
                    `
                })
            if (res.flag) {
                document.getElementById("web_more").style.display = "none";
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
})


document.getElementById("mobile_more").addEventListener('click', e=> {
    $.ajax({
        type: "POST",
        url: "/",
        data: {
            "csrfmiddlewaretoken": csrf,
            'from': mobile,
            "type": "mobile",
        },
        success: (res)=> {
            mobile = mobile + 2
            res.objects.forEach(i=> {
                    document.getElementById("mobile_projects_items").innerHTML +=  `
                        <div class="mobile_project">
                            <img src=${i.image} class="mobile_project_img">
                            <div class="mobile_project_data">
                                <div class="mobile_project_info" style="float: left;">
                                    <p class="mobile_project_name">${i.name}</p>
                                    <img src=${res.foto1} class="mobile_city_png"><p class="mobile_project_city">${i.city}</p>
                                    <img src=${res.foto2} class="mobile_floor_png"><p class="mobile_project_floor">${i.floor}</p>
                                </div>
                                <div style="float: right; font-family: Inter, sans-serif; margin-top: 20px;">
                                    <a href=${i.url} class="mobile_project_page">перейти к объекту</a><img src=${res.foto3}>
                                </div>
                            </div>
                        </div>
                    `
                })
            if (res.flag) {
                document.getElementById("mobile_more").style.display = "none";
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
})