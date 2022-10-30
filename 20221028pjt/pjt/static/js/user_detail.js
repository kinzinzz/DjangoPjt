const followBtn = document.getElementById('follow-btn')
const follower = document.getElementById('follower')
const follow = document.getElementById('follow')

followBtn.addEventListener('click', function (event) {

    axios({
        method: 'GET',
        url: `/accounts/${event.target.dataset.userId}/follow/`
    }).then(response => {

        if (response.data.self_follow) {
            follower.setAttribute('class', 'mt-2 mx-1')
            follow.setAttribute('class', 'mt-2 mx-1')
            follower.innerText = '팔로워: ' + response.data.userFollowings
            follow.innerText = '팔로우: ' + response.data.userFollowers
            alert('자신은 팔로잉 할 수 없습니다.')
        }
        else if (response.data.exited_user) {
            followBtn.innerText = '팔로우 취소'
        }
        else {
            followBtn.innerText = '팔로우'
        }
        follower.setAttribute('class', 'mt-2 mx-1')
        follow.setAttribute('class', 'mt-2 mx-1')
        follower.innerText = '팔로워: ' + response.data.userFollowings
        follow.innerText = '팔로우: ' + response.data.userFollowers
    })
})