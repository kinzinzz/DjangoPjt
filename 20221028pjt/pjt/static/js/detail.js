//비동기

// 댓글 
const comment_form = document.getElementById('comment_form');
// csrftoken
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

comment_form.addEventListener('submit', function (event) {
    event.preventDefault();

    axios(
        {
            method: 'POST',
            url: `/reviews/${event.target.dataset.reviewId}/comments/create/`,
            headers: { 'X-CSRFToken': csrftoken },
            data: new FormData(comment_form)

        }
    )

        .then(response => {
            // 댓글 삭제 버튼 비동기 추가
            const newCommentId = `${response.data.commentId}`
            const commentReviewId = `${response.data.commentReviewId}`
            const div_btn = document.createElement('div')
            const a = document.createElement('a')
            a.setAttribute('href', `/reviews/${commentReviewId}/comments/${newCommentId}/delete/`)
            div_btn.appendChild(a)
            a.innerText = '댓글삭제'

            // 댓글 비동기 추가
            const comments_body = document.getElementById('comments_body')
            const div = document.createElement('div')
            div.innerText = `${response.data.commentAuthorUsername}: ${response.data.commentContent}`
            comments_body.append(div, div_btn)


            // 첫댓글일 때 "아직 댓글이 없습니다" 없애기
            const comments_empty = document.getElementById('comments_empty')

            if (comments_empty) {
                comments_empty.style.display = 'none';
            }
            // 폼 리셋
            comment_form.reset()
        })

}

)



// 좋아요
// 좋아요 비동기

const likeBtn = document.querySelector('#like-btn')
likeBtn.addEventListener('click', function (event) {

    axios({
        method: 'GET',
        url: `/reviews/${event.target.dataset.reviewId}/like/`
    })
        .then(response => {
            if (response.data.existed_user === true) {
                event.target.classList.add('bi-heart-fill')
                event.target.classList.remove('bi-heart')

            }
            else {
                event.target.classList.add('bi-heart')
                event.target.classList.remove('bi-heart-fill')

            }
            const likeCount = document.querySelector('#like-count')
            likeCount.innerText = response.data.likeCount
        })
})

