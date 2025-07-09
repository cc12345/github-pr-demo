#!/bin/bash

# 部署脚本
# 用于将应用部署到不同环境

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 帮助信息
show_help() {
    echo "部署脚本使用说明"
    echo ""
    echo "用法: $0 [选项] <环境>"
    echo ""
    echo "环境:"
    echo "  staging    部署到预发布环境"
    echo "  production 部署到生产环境"
    echo ""
    echo "选项:"
    echo "  -h, --help      显示帮助信息"
    echo "  -v, --version   显示版本信息"
    echo "  -d, --dry-run   模拟部署，不执行实际操作"
    echo "  -f, --force     强制部署，跳过检查"
    echo ""
    echo "示例:"
    echo "  $0 staging              # 部署到预发布环境"
    echo "  $0 production --dry-run # 模拟生产环境部署"
    echo ""
}

# 版本信息
show_version() {
    echo "Deploy Script v1.0.0"
    echo "GitHub PR Demo Project"
}

# 检查环境
check_environment() {
    local env=$1
    
    log_info "检查部署环境: $env"
    
    case $env in
        staging)
            log_info "目标环境: 预发布环境"
            DEPLOY_HOST="staging.example.com"
            DEPLOY_PATH="/var/www/staging"
            ;;
        production)
            log_info "目标环境: 生产环境"
            DEPLOY_HOST="production.example.com"
            DEPLOY_PATH="/var/www/production"
            
            # 生产环境额外检查
            if [[ "$FORCE_DEPLOY" != "true" ]]; then
                log_warning "部署到生产环境需要额外确认"
                read -p "确定要部署到生产环境吗？(y/N) " -n 1 -r
                echo
                if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                    log_error "用户取消部署"
                    exit 1
                fi
            fi
            ;;
        *)
            log_error "未知的部署环境: $env"
            log_info "支持的环境: staging, production"
            exit 1
            ;;
    esac
}

# 运行测试
run_tests() {
    log_info "运行测试套件..."
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] 跳过测试执行"
        return 0
    fi
    
    # 运行测试
    if python -m pytest tests/ -v --tb=short; then
        log_success "所有测试通过"
    else
        log_error "测试失败，停止部署"
        exit 1
    fi
}

# 构建应用
build_app() {
    log_info "构建应用..."
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] 跳过构建过程"
        return 0
    fi
    
    # 清理旧的构建
    if [[ -d "dist" ]]; then
        rm -rf dist/
    fi
    
    # 构建包
    python -m build
    
    if [[ $? -eq 0 ]]; then
        log_success "构建完成"
    else
        log_error "构建失败"
        exit 1
    fi
}

# 部署应用
deploy_app() {
    local env=$1
    
    log_info "部署应用到 $env 环境..."
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] 模拟部署到 $DEPLOY_HOST:$DEPLOY_PATH"
        log_info "[DRY RUN] 部署步骤:"
        log_info "[DRY RUN]   1. 备份当前版本"
        log_info "[DRY RUN]   2. 上传新版本"
        log_info "[DRY RUN]   3. 更新配置"
        log_info "[DRY RUN]   4. 重启服务"
        log_info "[DRY RUN]   5. 健康检查"
        return 0
    fi
    
    # 实际部署步骤
    log_info "步骤 1/5: 创建备份..."
    # 这里添加实际的备份逻辑
    sleep 1
    log_success "备份完成"
    
    log_info "步骤 2/5: 上传新版本..."
    # 这里添加实际的上传逻辑
    sleep 2
    log_success "上传完成"
    
    log_info "步骤 3/5: 更新配置..."
    # 这里添加实际的配置更新逻辑
    sleep 1
    log_success "配置更新完成"
    
    log_info "步骤 4/5: 重启服务..."
    # 这里添加实际的服务重启逻辑
    sleep 2
    log_success "服务重启完成"
    
    log_info "步骤 5/5: 健康检查..."
    # 这里添加实际的健康检查逻辑
    sleep 1
    log_success "健康检查通过"
}

# 部署后验证
post_deploy_check() {
    local env=$1
    
    log_info "执行部署后验证..."
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] 跳过部署后验证"
        return 0
    fi
    
    # 模拟验证步骤
    log_info "验证服务状态..."
    sleep 1
    log_success "服务运行正常"
    
    log_info "验证接口可用性..."
    sleep 1
    log_success "接口响应正常"
    
    log_info "验证数据库连接..."
    sleep 1
    log_success "数据库连接正常"
}

# 发送通知
send_notification() {
    local env=$1
    local status=$2
    
    log_info "发送部署通知..."
    
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "[DRY RUN] 跳过通知发送"
        return 0
    fi
    
    local message
    if [[ "$status" == "success" ]]; then
        message="🎉 部署成功！应用已部署到 $env 环境"
    else
        message="❌ 部署失败！$env 环境部署过程中出现错误"
    fi
    
    # 这里可以添加实际的通知逻辑
    # 比如发送到 Slack、Discord 或邮件
    log_info "通知消息: $message"
    log_success "通知已发送"
}

# 主函数
main() {
    local environment=""
    local dry_run=false
    local force=false
    
    # 解析命令行参数
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_help
                exit 0
                ;;
            -v|--version)
                show_version
                exit 0
                ;;
            -d|--dry-run)
                dry_run=true
                shift
                ;;
            -f|--force)
                force=true
                shift
                ;;
            staging|production)
                environment=$1
                shift
                ;;
            *)
                log_error "未知参数: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # 检查必需参数
    if [[ -z "$environment" ]]; then
        log_error "请指定部署环境"
        show_help
        exit 1
    fi
    
    # 设置全局变量
    export DRY_RUN=$dry_run
    export FORCE_DEPLOY=$force
    
    # 部署流程
    log_info "开始部署流程..."
    log_info "环境: $environment"
    log_info "模式: $([ "$dry_run" == "true" ] && echo "模拟部署" || echo "实际部署")"
    
    # 执行部署步骤
    check_environment "$environment"
    run_tests
    build_app
    deploy_app "$environment"
    post_deploy_check "$environment"
    send_notification "$environment" "success"
    
    log_success "部署完成！"
}

# 错误处理
trap 'log_error "部署过程中出现错误，退出代码: $?"' ERR

# 运行主函数
main "$@"