<script>
    {% load static %}
</script>

$(function () {
    // Create  button
    $(".create-player").modalForm({
        formURL: "{% url 'players:create_player' %}"
    });
    $(".create-referee").modalForm({
        formURL: ""
    });
    $(".create-club").modalForm({
        formURL: "{% url 'main:create_club' %}"
    });
    $(".create-medical-report").modalForm({
        formURL: "{% url 'medical:create_medical' %}"
    });
    $(".create-snc-report").modalForm({
        formURL: "{% url 'snc:create_conditioning' %}"
    });
    $(".create-user").modalForm({
        formURL: "{% url 'accounts:create_user' %}"
    });
    $(".club-admin").modalForm({ formURL: "{% url 'main:club_admin' %}" });

    // Update buttons
    $(".update-player").each(function () {
        $(this).modalForm({ formURL: $(this).data("id") });
    });

    $(".update-verify").each(function () {
        $(this).modalForm({ formURL: $(this).data("id") });
    });

    // Read  buttons
    $(".player-details").each(function () {
        $(this).modalForm({ formURL: $(this).data("id") });
    });

    $(".club-view").each(function () {
        $(this).modalForm({ formURL: $(this).data("id") });
    });

    $(".snc-details").each(function () {
        $(this).modalForm({ formURL: $(this).data("id") });
    });

    // Delete  buttons
    $(".delete-player").each(function () {
        $(this).modalForm({ formURL: $(this).data("id") });
    });
});
