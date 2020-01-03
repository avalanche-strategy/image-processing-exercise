import axios from 'axios';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

if (!getCookie('csrftoken')) {
    axios.get('/csrf');
}

export default {
    post: (url, data) => axios.post(url, data, { headers: { 'X-CSRFToken': getCookie('csrftoken') } }),
    get: (url, data) => axios.get(url, data)
}