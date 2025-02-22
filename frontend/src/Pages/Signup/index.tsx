import axios from "axios";
import { useState } from "react";
import { Controller, SubmitHandler, useForm } from "react-hook-form";
import styled from "styled-components";
import NationBox from "../../Components/Nationoption/Selectbox";
import "./index.css";

interface IFormInput {
  email: string;
  password1: string;
  password2: string;
  nickName: string;
  firstName: string;
  lastName: string;
  nationality: string;
  phone: string;
  birth: Date;
  profession: string;
}

function SignUp() {
  const {
    register,
    handleSubmit,
    watch,
    control,
    formState: { errors },
  } = useForm<IFormInput>();

  const [loading, setLoading] = useState(false);

  const onSubmit: SubmitHandler<IFormInput> = async (data) => {
    setLoading(true);
    console.log(data);
    try {
      const response = await axios.post(
        "http://ec2-43-201-73-9.ap-northeast-2.compute.amazonaws.com:8000/api/accounts/",
        data,
        { withCredentials: true },
      );
      console.log(response);
    } catch (error) {
      alert(error.response?.data);
    }
    setLoading(false);
  };

  return (
    <div className="signup">
      <h1 className="signupTitle">회원가입</h1>
      <form className="signupForm" onSubmit={handleSubmit(onSubmit)}>
        <div className="signupInputDiv">
          <div className="signupDiv">이메일 주소</div>
          <div className="rightSignDiv">
            <input
              className="signupInput"
              placeholder="예: landing@landing.com"
              {...register("email", {
                required: true,
                pattern: {
                  value:
                    /^[A-Za-z0-9_]+[A-Za-z0-9]*[@]{1}[A-Za-z0-9]+[A-Za-z0-9]*[.]{1}[A-Za-z]{1,3}$/,
                  message: "이메일의 형식이 올바르지 않습니다.",
                },
              })}
              type="email"
              id="email"
              name="email"
            />
            {errors.email && <Message>{errors.email.message}</Message>}
          </div>
        </div>

        <div className="signupInputDiv">
          <div className="signupDiv">비밀번호</div>
          <div className="rightSignDiv">
            <input
              className="signupInput"
              placeholder="비밀번호를 입력해주세요."
              {...register("password1", {
                required: true,
                pattern: {
                  value:
                    /^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,20}$/,
                  message: "숫자+영문+특수문자 조합 8자리 이상 입력해주세요.",
                },
                deps: ["password2"],
              })}
              type="password"
              id="password1"
              name="password1"
            />
            {errors.password1 && <Message>{errors.password1.message}</Message>}
          </div>
        </div>
        <div className="signupInputDiv">
          <div className="signupDiv">비밀번호 확인</div>
          <div className="rightSignDiv">
            <input
              className="signupInput"
              placeholder="비밀번호를 다시 입력해주세요."
              {...register("password2", {
                required: true,
                validate: (value) =>
                  value === watch("password1")
                    ? true
                    : "비밀번호를 확인해 주세요.",
              })}
              type="password"
              id="password2"
              name="password2"
            />
            {errors.password2 && <Message>{errors.password2.message}</Message>}
          </div>
        </div>
        <div className="signupInputDiv">
          <div className="signupDiv">이용자 이름(닉네임)</div>
          <div className="rightSignDiv">
            <input
              placeholder="8글자 이내 한글로 적어주세요."
              className="signupInput"
              {...register("nickName", {
                required: true,
                maxLength: {
                  value: 8,
                  message: "8글자 이내로 입력해주세요.",
                },
                pattern: {
                  value: /^(?=.*[가-힣])[^0-9]{1,8}$/,
                  message:
                    "숫자,영어로 이루어진 이름(닉네임)은 사용하실 수 없습니다.",
                },
              })}
              type="text"
              id="nickName"
              name="nickName"
            />
            {errors.nickName && <Message>{errors.nickName.message}</Message>}
          </div>
        </div>
        <div className="signupInputDiv">
          <div className="signupDiv">국적</div>
          <div className="rightSignDiv">
            <Controller
              name="nationality"
              control={control}
              defaultValue="Korea, Republic of"
              rules={{ required: true }}
              render={({ field }) => <NationBox field={field} />}
            />
          </div>
        </div>
        <div className="signupInputDiv">
          <div className="signupDiv">이름 (First Name)</div>
          <div className="rightSignDiv">
            <input
              className="signupInput"
              {...register("firstName", {
                required: true,
                pattern: /^[A-Za-z|가-힣]{1,}$/,
              })}
              type="text"
              id="firstName"
              name="firstName"
            />
          </div>
        </div>
        <div className="signupInputDiv">
          <div className="signupDiv">성 (Last Name)</div>
          <div className="rightSignDiv">
            <input
              className="signupInput"
              {...register("lastName", {
                required: true,
                pattern: /^[A-Za-z|가-힣]{1,}$/,
              })}
              type="text"
              id="lastName"
              name="lastName"
            />
          </div>
        </div>
        <div className="signupInputDiv">
          <div className="signupDiv">휴대폰 번호</div>
          <div className="rightSignDiv">
            <input
              className="signupInput"
              placeholder="010-1234-1234"
              {...register("phone", {
                required: true,
                pattern: {
                  value: /^010-([0-9]{3,4})-([0-9]{4})$/,
                  message: "올바른 형식이 아닙니다.",
                },
              })}
              type="text"
              id="phone"
              name="phone"
            />
            {errors.phone && <Message>{errors.phone.message}</Message>}
          </div>
        </div>

        <div className="signupInputDiv">
          <div className="signupDiv">생년월일</div>
          <div className="rightSignDiv">
            <input
              className="signupInput"
              {...register("birth", {
                required: true,
                min: "1901-01-01",
                max: "2024-12-31",
              })}
              type="date"
              id="birth"
              name="birth"
            />
          </div>
        </div>
        <div className="signupInputDiv">
          <div className="signupDiv">직업</div>
          <div className="rightSignDiv">
            <input
              className="signupInput"
              {...register("profession", {
                required: false,
              })}
              type="text"
              id="profession"
              name="profession"
            />
          </div>
        </div>
        <div className="signupBtnBox">
          <button className="signupBtn" type="submit">
            회원가입
          </button>
        </div>
      </form>
    </div>
  );
}

export default SignUp;

const Message = styled.p`
  width: 176px;
  color: red;
  font-size: 0.85rem;
  margin-top: 5px;
  padding-left: 5px;
`;
