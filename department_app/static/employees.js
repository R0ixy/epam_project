$('.add_date').click(function () {
    $('.second_date').show();
    $('.hide_date').show();
    $('.add_date').hide();
})
$('.hide_date').click(function () {
    $('.second_date').hide();
    $('.add_date').show();
    $('.hide_date').hide();
})
$('.x').click(function () {
    $('div#window_emp').hide();
    $('.b-popup').hide();
})
$(document).ready(function () {
    $('body').on('click', '.edit', function () {
        const a = $(`#${this.dataset.id}`);
        const title = a.find('.department_title').html();
        let list = [];
        for (let i of a.find('b')) {
            list.push(i.innerHTML);
        }
        $('.input_name').val(title);
        $('#salary').val(list[2]);
        $('#position').val(list[3]);
        $('.title_add_emp').append(title);
        $(`select option[value='${list[4]}']`).prop('selected', true);
        $('div#window_emp').show();
        $('.b-popup').show();
    })
});


$('input[type="submit"].search').click(async function () {
    let first_date = $('input.first_date').val();
    const second_date = $('input.second_date').val();
    const dep_id = $('select.dep').val()
    let response = await fetch('/api/employee/?' + new URLSearchParams({
        'id': dep_id,
        'first_date': first_date,
        'second_date': second_date
    }))
    let result = await response.json()

    $('div.employee_block').remove();

    for (let i of result) {
        $('div.content').append(`<div class="employee_block" id="${i.id}">
                                        <h2 class="department_title">${i.full_name}</h2>
                                        <div class="employee_text_block">
                                            <div class="textcols-item">
                                                <p class="emp_text_left">Age: <b style="color:#0d6efd">${i.age}</b></p>
                                                <p class="emp_text_left">Birthday: <b style="color:#0d6efd">${i.date_of_birth}</b></p>
                                            </div>
                                            <div class="textcols-item">
                                                <p class="emp_text_center">Salary: <b style="color:#0d6efd">${i.salary}</b></p>
                                                <p class="emp_text_center">Position: <b style="color:#0d6efd">${i.position}</b></p>
                                            </div>
                                            <div class="textcols-item">
                                                <p class="emp_text_right">Department: <b style="color:#0d6efd">Department two</b></p>
                                            </div>
                                        </div>
                                        <div class="department_button">
                                            <p>
                                                <input type="button" class="edit" data-id="1" value="Edit">
                                            </p>
                                            <form action="/delete/1" method="post">
                                                <p>
                                                    <input type="button" class="delete" value="Delete">
                                                </p>
                                            </form>
                                
                                        </div>
                                    </div>`);
    }
});