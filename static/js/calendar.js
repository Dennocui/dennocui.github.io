<script>

    $(document).ready(function () {
      var calendar = $('#calendar').fullCalendar({
        header: {
        left: 'prev,next today',
    center: 'title',
    right: 'month,agendaWeek,agendaDay'
  },
  events: [
          {% for event in events %}
                        {
        title: "{{ event.name }}",
          start: '{{ event.start | date:"Y-m-d" }}',
          end: '{{ event.end | date:"Y-m-d" }}',
          id: '{{ event.id }}',
  },
        {% endfor %}
    ],
selectable: true,
selectHelper: true,
editable: true,
eventLimit: true,
      select: function (start, end, allDay) {
        var title = prompt("Enter Event Title");
        if (title) {
          var start = $.fullCalendar.formatDate(start, "Y-MM-DD HH:mm:ss");
    var end = $.fullCalendar.formatDate(end, "Y-MM-DD HH:mm:ss");
          $.ajax({
        type: "GET",
    url: 'main/add_event',
            data: {'title': title, 'start': start, 'end': end },
    dataType: "json",
            success: function (data) {
        calendar.fullCalendar('refetchEvents');
    alert("Added Successfully");
  },
            failure: function (data) {
        alert('There is a problem!!!');
  }
});
}
},
      eventResize: function (event) {
        var start = $.fullCalendar.formatDate(event.start, "Y-MM-DD HH:mm:ss");
    var end = $.fullCalendar.formatDate(event.end, "Y-MM-DD HH:mm:ss");
    var title = event.title;
    var id = event.id;
        $.ajax({
        type: "GET",
    url: '/update',
          data: {'title': title, 'start': start, 'end': end, 'id': id },
    dataType: "json",
          success: function (data) {
        calendar.fullCalendar('refetchEvents');
    alert('Event Update');
  },
          failure: function (data) {
        alert('There is a problem!!!');
  }
});
},

      eventDrop: function (event) {
        var start = $.fullCalendar.formatDate(event.start, "Y-MM-DD HH:mm:ss");
    var end = $.fullCalendar.formatDate(event.end, "Y-MM-DD HH:mm:ss");
    var title = event.title;
    var id = event.id;
        $.ajax({
        type: "GET",
    url: '/update',
          data: {'title': title, 'start': start, 'end': end, 'id': id },
    dataType: "json",
          success: function (data) {
        calendar.fullCalendar('refetchEvents');
    alert('Event Update');
  },
          failure: function (data) {
        alert('There is a problem!!!');
  }
});
},

      eventClick: function (event) {
        if (confirm("Are you sure you want to remove it?")) {
          var id = event.id;
          $.ajax({
        type: "GET",
    url: '/remove',
            data: {'id': id },
    dataType: "json",
            success: function (data) {
        calendar.fullCalendar('refetchEvents');
    alert('Event Removed');
  },
            failure: function (data) {
        alert('There is a problem!!!');
  }
});
}
},

  });
});

  </script>